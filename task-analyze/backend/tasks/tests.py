from django.test import TestCase
from .scoring import score_task, detect_cycle

class ScoringTests(TestCase):
    def test_fastest_prioritizes_low_effort(self):
        t1 = {"id": "A", "title": "small", "estimated_hours": 0.5, "importance": 5, "due_date": None, "dependencies": []}
        t2 = {"id": "B", "title": "big", "estimated_hours": 20, "importance": 5, "due_date": None, "dependencies": []}
        s1, _ = score_task(t1, {"A": t1, "B": t2}, strategy="fastest")
        s2, _ = score_task(t2, {"A": t1, "B": t2}, strategy="fastest")
        self.assertTrue(s1 > s2)

    def test_deadline_prioritizes_due_soon(self):
        from datetime import datetime, timedelta
        soon = (datetime.utcnow().date() + timedelta(days=1)).isoformat()
        later = (datetime.utcnow().date() + timedelta(days=30)).isoformat()
        t1 = {"id": "A", "title": "soon", "estimated_hours": 5, "importance": 5, "due_date": soon, "dependencies": []}
        t2 = {"id": "B", "title": "later", "estimated_hours": 1, "importance": 5, "due_date": later, "dependencies": []}
        s1, _ = score_task(t1, {"A": t1, "B": t2}, strategy="deadline")
        s2, _ = score_task(t2, {"A": t1, "B": t2}, strategy="deadline")
        self.assertTrue(s1 > s2)

    def test_detect_cycle(self):
        edges = {"A": ["B"], "B": ["C"], "C": ["A"]}
        cyc = detect_cycle(edges)
        self.assertTrue(len(cyc) > 0)
