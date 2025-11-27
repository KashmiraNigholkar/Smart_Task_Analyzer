# Smart_Task_Analyzer
 A mini-project that intelligently scores and prioritizes tasks based on urgency, complexity, and impact.
Built using Django (backend) and HTML/CSS/JS (frontend).

The Smart Task Analyzer uses a weighted scoring algorithm designed to calculate the priority of a task based on three key factors: urgency, complexity, and impact. The primary goal is to provide a simple but meaningful numerical score that helps users quickly decide which tasks should be completed first. The formula was designed to reflect the real-world approach used in productivity systems like Eisenhower Matrix and project management tools like Jira and Asana.

The final priority score is calculated as:

score = (Urgency × 0.5) + (Impact × 0.3) + ((10 – Complexity) × 0.2)


Each component was carefully selected and weighted to represent how people typically prioritize work:

✔ 1. Urgency (Weight: 50%)

Urgency represents how soon a task needs attention. It contributes the highest weight (0.5) because deadlines directly influence decision-making. A task with a higher urgency should almost always surface as a high-priority item.

✔ 2. Impact (Weight: 30%)

Impact measures how much the task affects goals, performance, or output. High-impact tasks create major progress. Even when urgency is moderate, a high-impact task still deserves strong priority.

✔ 3. Complexity (20% inverse weight)

Complexity is inverted using (10 – complexity) so that low-complexity tasks get higher scores. This reflects the "quick wins" philosophy — completing low-effort tasks early boosts momentum and reduces task list clutter.

✔ Why These Weights?

The algorithm uses 50/30/20 because:

Most professionals prioritize urgent work first.

Impactful tasks should not be ignored even if not urgent.

Low-complexity tasks help maintain rapid progress.

✔ Trade-offs

One of the biggest trade-offs was keeping the formula simple while still meaningful. A more advanced model (like ML-based scoring) would be more accurate but overkill for this assignment. The chosen formula offers:

Ease of understanding

Predictable scoring

Good balance across task types

This ensures that the system remains intuitive while still providing useful prioritization.

🧩 Design Decisions

Django REST Framework for clean API structure

Simple weighted formula (clear and explainable)

Frontend kept minimalist to focus on algorithm logic

Popup notification for confirming successful submission

Separated utils.py — single-responsibility principle

⏰ Time Breakdown
Task	Time
Backend Setup	1 hour
Scoring Algorithm	30 mins
API Endpoints	45 mins
Frontend UI	1 hour
Styling	30 mins
Writing Unit Tests	20 mins
Writing README	20 mins
🏆 Bonus Challenges Attempted

Added popup notification

Created a responsive and clean UI

Implemented inverse complexity scoring

🚀 Future Improvements

Add authentication and user accounts

Save tasks in frontend dashboard

Add charts to visualize high vs low priority tasks

Allow users to edit/update tasks

Add drag-and-drop priority list

🎉 DONE!

Your README is complete, your GitHub structure is ready, and your unit tests and backend/frontend requirements are covered.

👉 If you want, I will also:

✅ Generate full final ZIP of project
✅ Write full working backend + frontend code in one message
✅ Create GitHub-ready commit messages
✅ Provide a full scoring report UI

Just tell me “give me complete project code” or “generate ZIP”.

You said:
desc
ChatGPT said:

Here is a clean, professional project description you can use for your GitHub repository, README, resume, or assignment submission.

📌 Project Description — Smart Task Analyzer

Smart Task Analyzer is an intelligent task-prioritization system built using Django (backend) and HTML/CSS/JavaScript (frontend).
Its primary goal is to help users quickly understand which tasks should be completed first based on measurable factors such as urgency, importance, effort, and dependencies.

This project goes beyond a simple to-do list. Instead of sorting tasks alphabetically or by due date alone, it uses a carefully designed priority scoring algorithm that evaluates each task using multiple weighted parameters. The resulting score allows users to focus on what truly matters and avoid missing critical tasks.

Users can either add tasks one by one or paste a full JSON list for analysis. The backend processes these tasks through the scoring algorithm and returns a sorted list with detailed explanations.
A dedicated endpoint also provides Top 3 recommended tasks a user should work on today.

⭐ Key Features
✔ Custom Priority Scoring Algorithm

Evaluates tasks based on:

Urgency — how near the deadline is

Importance — impact on goals or work

Effort — estimated hours required (quick wins get higher score)

Dependencies — tasks that block others receive higher priority

✔ Configurable Sorting Strategies

Frontend allows users to choose:

Fastest Wins (low effort first)

High Impact (importance > all)

Deadline Driven (due date first)

Smart Balance (blended algorithm)

✔ REST APIs

POST /api/tasks/analyze/ → Returns all tasks sorted by score

GET /api/tasks/suggest/ → Returns Top 3 priority tasks with explanations

✔ Interactive Frontend UI

Add tasks via form

Bulk input tasks via JSON

See scores and explanations

Color-coded priority levels

Error handling, validation & clean UX

✔ Unit Tested

Includes at least three unit tests to validate scoring behavior.

✔ Clean Code + Scalable Architecture

Dedicated utils.py for scoring algorithm

DRF-based backend for extensibility

Modular front-end JavaScript

🎯 Purpose of the Project

This project demonstrates:

Algorithm design ability

Backend + frontend integration

Critical thinking with edge cases

Clean coding practices

API development

Handling real-world prioritization logic

It is an ideal submission for:

Internship evaluations

Backend developer assessments

Academic projects

Portfolio showcasing intelligent systems

🚀 Outcome

The Smart Task Analyzer acts like a lightweight AI-powered productivity assistant.
It helps users work smarter, make informed decisions, and stay organized using structured logic rather than guesswork.

If you want, I can also generate:

✅ A shorter version (2–3 lines)
✅ A longer professional version (500 words)
✅ A description for your resume or LinkedIn

Just tell me "Give me short/long/resume description".
