from datetime import date, datetime, timedelta
import math
from collections import defaultdict, deque

def days_until_due(due_date: date):
    if due_date is None:
        return None
    today = datetime.utcnow().date()
    return (due_date - today).days

def normalize(val, min_v, max_v):
    if val is None:
        return 0.0
    val = max(min_v, min(max_v, val))
    if max_v == min_v:
        return 0.0
    return (val - min_v) / (max_v - min_v)

def detect_cycle(edges):
    """
    edges: dict node -> list of neighbors (dependency graph)
    returns list of nodes in a cycle or [] if none.
    Uses Kahn's topological detect; if nodes remain, cycle exists.
    """
    indeg = defaultdict(int)
    for u in edges:
        for v in edges[u]:
            indeg[v] += 1
    q = deque([u for u in edges if indeg[u] == 0])
    visited = 0
    while q:
        u = q.popleft()
        visited += 1
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if visited != len(edges):
        # return nodes that are part of cycles (indeg>0)
        return [n for n, d in indeg.items() if d > 0]
    return []

def score_task(task_dict, all_tasks_map, strategy="smart_balance", weights=None):
    """
    task_dict: dict with keys title, due_date (ISO string or None), estimated_hours, importance (1..10), dependencies (list of IDs)
    all_tasks_map: dict id -> task_dict
    strategy: 'fastest', 'high_impact', 'deadline', 'smart_balance'
    returns (score_float_0_100, explanation)
    """
    # default weights (smart balance)
    default_weights = {
        "importance": 0.35,
        "urgency": 0.25,
        "effort": 0.15,
        "dependency": 0.15,
        "past_due_boost": 0.10,  # applied multiplicatively
    }
    if weights:
        default_weights.update(weights)

    # parse fields
    importance = task_dict.get("importance") or 5
    importance = max(1, min(10, int(importance)))

    estimated_hours = task_dict.get("estimated_hours") or 1.0
    try:
        estimated_hours = float(estimated_hours)
    except Exception:
        estimated_hours = 1.0
    estimated_hours = max(0.0, estimated_hours)

    due_raw = task_dict.get("due_date")
    due_date = None
    if due_raw:
        try:
            due_date = datetime.fromisoformat(due_raw).date() if isinstance(due_raw, str) else due_raw
        except Exception:
            due_date = None

    days = days_until_due(due_date) if due_date else None

    # urgency score: if past due -> 1.0 and boost
    if days is None:
        urgency_score = 0.15
    else:
        if days <= 0:
            urgency_score = 1.0
        else:
            # smooth decay; 1 day -> ~1.0, 7 -> ~0.8, 30->~0.5, 90->~0.2
            urgency_score = max(0.0, min(1.0, 1.0 - math.log1p(days)/math.log1p(90)))

    # importance normalized 1..10 -> 0..1
    importance_n = (importance - 1) / 9.0

    # effort: lower hours -> higher score (quick wins)
    # invert and cap at 40 hours
    h = min(max(estimated_hours, 0.01), 40.0)
    effort_n = 1.0 - ((h - 0.01) / (40.0 - 0.01))

    # dependency score: number of tasks that depend on this task (i.e., how many it blocks)
    # all_tasks_map: id - >dict containing 'dependencies' list
    dependents_count = 0
    for other in all_tasks_map.values():
        deps = other.get("dependencies") or []
        if task_dict.get("id") in deps:
            dependents_count += 1
    # normalize number of dependents assuming 0..10 range
    dependency_n = normalize(dependents_count, 0, 10)

    # past due boost multiplier
    past_due_multiplier = 1.0
    if days is not None and days <= 0:
        past_due_multiplier += default_weights.get("past_due_boost", 0.1)

   
    if strategy == "fastest":
        score_components = (
            0.10 * importance_n +
            0.10 * urgency_score +
            0.70 * effort_n +
            0.10 * dependency_n
        )
    elif strategy == "high_impact":
        score_components = (
            0.75 * importance_n +
            0.10 * urgency_score +
            0.05 * effort_n +
            0.10 * dependency_n
        )
    elif strategy == "deadline":
        score_components = (
            0.10 * importance_n +
            0.75 * urgency_score +
            0.05 * effort_n +
            0.10 * dependency_n
        )
    else:  
        w = default_weights
        score_components = (
            w["importance"] * importance_n +
            w["urgency"] * urgency_score +
            w["effort"] * effort_n +
            w["dependency"] * dependency_n
        )

    raw_score = max(0.0, min(1.0, score_components))
    final_score = raw_score * 100 * past_due_multiplier
    final_score = min(100.0, final_score)

    explanation = {
        "importance_n": round(importance_n, 3),
        "urgency_n": round(urgency_score, 3),
        "effort_n": round(effort_n, 3),
        "dependency_n": round(dependency_n, 3),
        "dependents_count": dependents_count,
        "past_due_days": days,
        "raw_score": round(raw_score, 4),
        "final_score": round(final_score, 2),
        "strategy": strategy
    }

    return final_score, explanation
