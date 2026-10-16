# Job Search Portal

> A Flask and SQLite prototype exploring account registration, session-based login, and a job-portal interface.

**Python · Flask · SQLite · HTML · CSS**

## Overview

This project connects a simple authentication backend to server-rendered pages. Visitors can register, sign in, and move through a welcome screen to the portal home page. It demonstrates an early full-stack workflow: forms → validation → database queries → sessions → templates.

## Implemented features

- Registration with password confirmation and duplicate-username checks.
- Login backed by SQLite and parameterized database queries.
- Session checks on the main and home pages.
- Feedback messages for unsuccessful sign-in and registration attempts.

## Run locally

```bash
git clone https://github.com/Pandiyaraj2004/job_search_portal_project.git
cd job_search_portal_project/pro
python -m pip install flask
python app.py
```

Open http://localhost:5000. Run from `pro/` because the SQLite database path is relative to the working directory. Use fictional test accounts.

## Explore the code

| File | Purpose |
| --- | --- |
| [pro/app.py](pro/app.py) | Routes, database initialization, authentication, sessions |
| [pro/templates](pro/templates) | Login, registration, welcome, and home pages |
| [pro/static](pro/static) | Styling and image assets |

## Project scope

The backend currently implements account access and page navigation; it does not implement job posting, application tracking, or a job-search API. Before public deployment, replace the fixed session secret, use a dedicated password-hashing scheme instead of plain SHA-256, and disable debug mode.

---

Built by **Pandiyaraj A** · [Portfolio](https://pandiyaraj.netlify.app/) · [GitHub](https://github.com/Pandiyaraj2004) · [LinkedIn](https://www.linkedin.com/in/pandiyaraj-a-mca/)
