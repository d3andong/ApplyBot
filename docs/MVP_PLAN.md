# MVP Plan

## Overview
The MVP (Minimum Viable Product) now includes the ability for users to sign in, upload and parse their resume, set job preferences, view scraped job listings, and use a “helper flow” to practice or partially automate job applications. While some details will evolve, this MVP aims to provide a coherent end-to-end experience.

## Core Features for MVP

1. **User Authentication (Google OAuth + JWT):**
   - Users log in with Google.
   - On success, issue a JWT token stored as an HTTP-only cookie.
   - Store user info (google_id, email, name) in `users` table.

2. **Resume Upload & Parsing (with GPT-4):**
   - Users upload PDF/DOCX resumes.
   - Extract text using `pdfplumber` or `mammoth`.
   - Use GPT-4 to parse skills, experience, and education.
   - Store parsed data in `resumes` table.

3. **User Preferences:**
   - Users set roles, work arrangement (remote/onsite/hybrid), location, industries, experience years, salary range.
   - Store preferences in `user_preferences` table.
   - Preferences guide which jobs are shown.

4. **Job Scraping (at least one source, e.g. Indeed):**
   - Implement initial scraping using JobSpy or a basic scraper for a single job board (e.g., Indeed).
   - Run a daily scrape (or on-demand) to populate a `jobs` table.
   - Filter jobs by user preferences (basic filtering for roles, remote vs. onsite, location).

5. **Helper Flow for Job Applications:**
   - Provide an endpoint or UI flow where the user can “practice” applying to a sample job from our scraped listings.
   - GPT-4 assists by proposing answers to application questions.
   - The user reviews, edits, and provides feedback to improve answers.
   - Consider a minimal Chrome extension or simple front-end approach to show how these answers can be integrated into actual job applications.
   - MVP: Show at least one example application flow to confirm feasibility.

6. **API Endpoints (FastAPI):**
   - `/auth/google` and `/auth/google/callback`: OAuth flow.
   - `/auth/me`: Verify token, return user info.
   - `/resume/upload`: Upload and parse resume.
   - `/preferences` (GET/POST): Manage user preferences.
   - `/jobs/eligible`: Return scraped jobs filtered by preferences.
   - `/helper-flow`: Initiate a helper session to fill out an application form and provide GPT-assisted answers.

## Non-Functional Requirements
- Simple tests with `pytest`.
- Basic CI pipeline on GitHub Actions for test runs.
- `.env` for secrets and configs.
- Logging and error handling at a basic level.

## Out of Scope for MVP
- Advanced multi-board scraping beyond a single source (initially just Indeed).
- Automatic application submission beyond a simple helper demonstration.
- Payment integration or subscription model.
- Detailed UI: focus on backend endpoints and possibly a minimal extension or HTML form to demo the helper flow.

## Deployment & Next Steps
- Initially run locally with Docker for Postgres.
- After MVP stable: add more job boards, refine helper flow, consider scaling scraping and integrating a full Chrome extension or UI. Later, integrate payment and subscription logic.
