const API_URL = "http://127.0.0.1:8000/api/tasks/";

// Load tasks on page load
document.addEventListener("DOMContentLoaded", fetchTasks);

// Submit form
document.getElementById("taskForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const payload = {
    title: title.value,
    description: description.value,
    urgency: Number(urgency.value),
    importance: Number(importance.value),
    time_required: Number(time_required.value),
    deadline: deadline.value || null,
  };

  // Send POST request
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    Swal.fire("Error", "Failed to add task", "error");
    return;
  }

  // Success popup
  Swal.fire({
    title: "Task Added!",
    text: "Your task has been added successfully.",
    icon: "success",
    timer: 1500,
    showConfirmButton: false,
  });

  document.getElementById("taskForm").reset();

  fetchTasks();
});

// Fetch tasks from backend
async function fetchTasks() {
  const container = document.getElementById("taskList");
  container.innerHTML = "";

  try {
    const res = await fetch(API_URL);

    if (!res.ok) return;

    const tasks = await res.json();

    tasks.forEach((task) => renderTask(task));
  } catch (err) {
    console.log("Error loading tasks:", err);
  }
}

// Render each task as card
function renderTask(task) {
  const container = document.getElementById("taskList");

  const card = document.createElement("div");
  card.className = "task-card";

  const priority =
    task.urgency >= 4 || task.importance >= 4
      ? "high"
      : task.urgency >= 2 || task.importance >= 2
      ? "medium"
      : "low";

  card.innerHTML = `
    <div class="task-header">
      <h3>${task.title}</h3>
      <span class="badge badge-${priority}">${priority.toUpperCase()}</span>
    </div>
    <p>${task.description}</p>
    <p><strong>Urgency:</strong> ${task.urgency} | 
       <strong>Importance:</strong> ${task.importance} |
       <strong>Time:</strong> ${task.time_required} hr</p>
    <p><strong>Deadline:</strong> ${task.deadline ?? "No deadline"}</p>
  `;

  container.appendChild(card);
}
