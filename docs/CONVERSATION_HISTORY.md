# Conversation History

## Overview
This document records the evolution of our project’s purpose, technical decisions, and contextual details. It serves as a reference for why and how the project developed in its current form.

## Project Purpose
The primary goal of this project is to **streamline the job application process**. We aim to help users find relevant job listings, parse their resumes with GPT, set preferences, and even practice or partially automate filling out job applications. The MVP focuses on establishing a solid foundation for these features.

## Key Decisions Timeline

1. **Initial Node.js Approach:**
   - Started with Node.js + Express + TypeScript.
   - Users authenticate with Google OAuth, upload resumes for GPT parsing, set preferences, and (initially) we planned scraping and helper flow for after MVP.
   
2. **Expanding MVP Scope to Include Scraping & Helper Flow:**
   - Later decided to include job scraping (at least from Indeed) and a helper flow in the MVP.
   - Helper flow: GPT-assisted Q&A for job applications, potentially demonstrated via a minimal UI or a Chrome extension.

3. **Switching to Python + FastAPI:**
   - We recognized Python’s strengths for data and AI tasks.
   - Chose Python + FastAPI for unified stack and easier integration with GPT and scraping tools (like JobSpy).
   - Agreed to start fresh in a new `backend_python` directory.

4. **GPT Project Integration:**
   - Decided to use GPT’s project feature to maintain code context, making iterative development more efficient.
   - Established `PROMPTING_GUIDELINES.md` to standardize how we prompt GPT and maintain code quality.

5. **Documentation and Context Preservation:**
   - `MVP_PLAN.md`: Defines the core MVP features (auth, resume parsing, preferences, scraping, helper flow).
   - `SCRAPING_PLANS.md`: Details how we’ll implement initial scraping from Indeed and expand later.
   - `PROMPTING_GUIDELINES.md`: Explains how to craft prompts for GPT, both for user features (resume parsing, helper flow) and developer workflows.
   - `CONVERSATION_HISTORY.md` (this file): Summarizes decisions and evolution.

6. **Developer Environment & Terminal Context:**
   - Developer’s local environment is indicated by a prompt like:
     ```
     deaneyolfson@Deans-Air backend_python %
     ```
   - This reflects a macOS environment with a directory named `backend_python`. Future instructions or terminal commands can reference this prompt for clarity.
   - Example:
     ```bash
     deaneyolfson@Deans-Air backend_python % uvicorn app.main:app --reload
     ```
   - Storing environment details helps when writing explicit commands or referencing the user’s current directory structure.

7. **Next Steps:**
   - With these docs and the MVP plan in place, we’ll proceed to implement features and refine the system iteratively.
   - Ongoing Q&A sessions will further refine scraping logic, helper flow details, and prompt engineering strategies.

## Key Takeaways
- The project’s end goal: streamline job applications with GPT-driven resume parsing, preferences, scraping, and helper flows.
- Technology stack moved from Node.js to Python for better synergy with AI and scraping tools.
- MVP now includes minimal scraping and a helper flow demonstration.
- Clear documentation and a project-like GPT workflow ensure efficient development and evolution.
- Explicitly noting the developer’s environment and shell prompt aids in writing accurate terminal commands.
