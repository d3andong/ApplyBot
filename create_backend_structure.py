#!/usr/bin/env python3
import os

# Define the structure of the project.
project_structure = {

    "app": {
        "main.py": "",
        "config.py": "",
        "db.py": "",
        "models": {
            "user.py": "",
            "user_preferences.py": "",
            "resume.py": ""
        },
        "routers": {
            "auth.py": "",
            "preferences.py": "",
            "resume.py": ""
        },
        "services": {
            "gpt_service.py": "",
            "oauth_service.py": "",
            "resume_parser.py": ""
        },
        "utils": {
            "jwt_utils.py": ""
        }
    },
    "tests": {},
    "docs": {
        "MVP_PLAN.md": "# MVP Plan\n\nThis document outlines the MVP plan.",
        "SCRAPING_PLANS.md": "# Scraping Plans\n\nThis document describes scraping approaches.",
        "PROMPTING_GUIDELINES.md": "# Prompting Guidelines\n\nThis document provides prompting guidelines.",
        "CONVERSATION_HISTORY.md": "# Conversation History\n\nThis document will store conversation history."
    },
    ".env": "SECRET_KEY=your-secret-key\nDB_URI=your-db-uri\n",
    "requirements.txt": "# Example requirements\nfastapi\nuvicorn\npydantic\nsqlalchemy\n",
    "README.md": "# Project Title\n\nA short description of the project."
}


def create_structure(base_path, structure):
    """Recursively create directories and files from a nested dictionary structure."""
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # This is a directory
            if not os.path.exists(current_path):
                os.makedirs(current_path)
                print(f"Created directory: {current_path}")
            else:
                print(f"Directory already exists: {current_path}")
            # Recurse into the directory
            create_structure(current_path, content)
        else:
            # This is a file
            if not os.path.exists(current_path):
                with open(current_path, 'w') as f:
                    f.write(content)
                print(f"Created file: {current_path}")
            else:
                print(f"File already exists: {current_path}")

if __name__ == '__main__':
    # Use the current working directory as the root directory
    root_directory = os.getcwd()
    create_structure(root_directory, project_structure)
    print("Project structure setup complete.")
