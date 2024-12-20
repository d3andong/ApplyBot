import os
from dotenv import load_dotenv

# Load variables from .env
# Ensure you're running your commands in `backend_python` directory so .env is found.
load_dotenv()  

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
JWT_SECRET = os.getenv("JWT_SECRET", "some_secret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
SESSION_SECRET = os.getenv("SESSION_SECRET", "some_session_secret")

# Print for debugging (optional, remove later when confirmed)
print("GOOGLE_CLIENT_ID:", GOOGLE_CLIENT_ID)
print("GOOGLE_CLIENT_SECRET:", GOOGLE_CLIENT_SECRET)
print("JWT_SECRET:", JWT_SECRET)
print("JWT_ALGORITHM:", JWT_ALGORITHM)
print("SESSION_SECRET:", SESSION_SECRET)
