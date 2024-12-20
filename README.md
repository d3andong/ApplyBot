# ApplyBot Backend (Python + FastAPI)

## Overview
This backend aims to streamline job applications by providing:

- **Google OAuth + JWT** for user authentication.
- **Resume parsing using GPT-4** to extract structured data.
- **User preferences** (roles, arrangement, location, etc.) stored in a Postgres database.
- **Job scraping** (initially from Indeed) integrated with preferences to show relevant listings.
- **Helper flow** allowing GPT-assisted application Q&A, demonstrating partial automation of job applications.

## Current Status
- **Stack:** Python 3 (Homebrew-installed), FastAPI, SQLModel, Docker-based Postgres, and Uvicorn.
- **Environment:** Virtual environment set up with `python3 -m venv --upgrade-deps venv`.
- **Database:** `user` and `userpreferences` tables created. Connection verified.
- **Basic Endpoint:** `/health` returns `{"status":"ok"}`.
- **Testing:** `pytest` functional; basic health test works.

## GitHub Integration
We have a GitHub repository to store and version control our code. As we implement each MVP feature, we will:

1. **Commit Often:** After completing a small feature or passing tests, run:
   ```bash
   git add .
   git commit -m "Implement [feature], passing tests"

Completed Steps
Environment & Tooling:

Python installed via Homebrew.
Virtual environment created and activated.
Dependencies like fastapi, uvicorn[standard], sqlmodel, psycopg2-binary, and pytest installed.
Database Setup:

docker compose up -d to start Postgres.
app/db.py with init_db() creates tables.
User and UserPreferences models implemented with JSONB fields for lists.
Verified tables via psql \dt command.
Health Check & Testing:

/health endpoint works.
Simple test_health.py test runs with python3 -m pytest.
Confirmed environment stable for further development.
Next Steps
Authentication (Google OAuth + JWT):

Implement auth.py for /auth/google and /auth/google/callback.
Issue JWTs on successful login.
Add /auth/me to verify user identity.
After completing, commit changes and push to GitHub.
Preferences Endpoint:

GET /preferences and POST /preferences routes in preferences.py.
Test by setting preferences for a logged-in user.
Commit and push changes.
Resume Parsing & GPT Integration:

resume_parser.py to extract PDF/DOCX text.
gpt_service.py to call GPT for structuring resume data.
/resume/upload endpoint to save parsed data.
Test, then commit and push updates.
Scraping & Helper Flow (MVP):

Minimal scraping script (scrape_jobs.py) for Indeed data.
Insert results into jobs table.
Add /jobs/eligible for filtered listings.
/helper-flow to demo GPT Q&A for applications.
Test each part, commit, and push.
Running & Testing
Run Server:

bash
Copy code
python3 -m uvicorn app.main:app --reload
Visit http://localhost:8000/health.

Run Tests:

bash
Copy code
python3 -m pytest
GitHub CI: We will add a GitHub Actions workflow for CI testing soon. Until then, manually run tests before pushing.

Documentation
docs/MVP_PLAN.md: Detailed MVP features.
docs/SCRAPING_PLANS.md: Scraping strategy.
docs/PROMPTING_GUIDELINES.md: GPT prompt conventions.
docs/CONVERSATION_HISTORY.md: Context and decisions.
Contact / Further Development
As we add features, we’ll continuously update this README, commit and push changes to GitHub, and refer to documentation and previous Q&As for guidance.