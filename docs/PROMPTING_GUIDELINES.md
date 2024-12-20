# Prompting Guidelines

## Overview
This document outlines the conventions and best practices for creating and refining GPT prompts in our project. It covers both end-user features (resume parsing, helper flow for applications) and developer workflows (e.g., how we use GPT’s project feature to aid coding).

## End-User Facing Prompts

1. **Resume Parsing Prompts:**
   - **Goal:** Extract structured information (skills, experience, education) from a raw resume text.
   - **Approach:**
     - Provide the entire extracted resume text as input.
     - Use a system or user message instructing GPT to return key fields (skills, roles, years of experience, education) in a structured JSON-like format if possible.
   - **Example Prompt:**
     ```
     System: "You are an assistant that extracts key details from resumes."
     User: "Extract skills, experiences, and education from the following resume text:\n[RESUME_TEXT]"
     ```
   - **Refinement:** If GPT’s response is inconsistent, add instructions like “Return the data as a JSON object with keys: skills, experience, education.”

2. **Helper Flow for Job Applications:**
   - **Goal:** GPT assists the user by generating answer suggestions for application form questions.
   - **Approach:**
     - The prompt includes the job description and the application questions.
     - Ask GPT to tailor answers based on the user’s resume data and preferences.
   - **Example Prompt:**
     ```
     System: "You are an assistant that helps write professional job application answers."
     User: "Given the resume data:\n[RESUME_DATA]\nAnd this job description:\n[JOB_DESCRIPTION]\nPlease draft answers to the following application questions:\n[QUESTIONS]"
     ```
   - **Refinement:** If user feedback indicates answers are too long or not formal enough, add style constraints: “Be concise and use a professional tone.”

## Developer / Internal Prompts

1. **Code Assistance with GPT Project Integration:**
   - **Goal:** Ask GPT to modify code files, add tests, or refactor functions.
   - **Approach:**
     - Provide GPT with file names and the relevant code sections.
     - Use clear instructions: "Open `app/services/gpt_service.py` and add a function `parse_resume_with_gpt(text: str) -> dict` that calls `openai.ChatCompletion.create`."
   - **Best Practices:**
     - Always specify the file or section to edit.
     - Give GPT a brief summary of what the code should do before asking for modifications.
     - Confirm changes by reviewing GPT’s proposed output and then apply it locally.

2. **Prompts for Refining Prompts:**
   - **Goal:** Sometimes we’ll iterate on prompts to improve GPT responses.
   - **Approach:**
     - Start with a baseline prompt and if results are suboptimal, ask GPT how to improve the prompt.
     - Test changes incrementally and document what worked best in this file for future reference.

## Style and Consistency

- **Be Explicit and Structured:** GPT responds better when given clear roles, instructions, and desired output formats.
- **Use System Messages for Role/Persona:** For tasks like resume parsing, define GPT’s role clearly at the start.
- **Iteration:** If an initial prompt doesn’t yield good results, log what didn’t work and try adding more constraints or examples.
- **Examples and Few-Shot Learning:** Provide GPT with one or two examples of desired output if complexity is high.

## Future Improvements

- After MVP launch, consider maintaining a library of known-good prompt templates in a `prompts/` directory.
- Add versioning to prompts: keep track of which prompt versions performed best for resume parsing and helper flow.

