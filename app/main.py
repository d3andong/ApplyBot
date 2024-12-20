from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import os
from app.config import SESSION_SECRET


from app.routers import auth

SESSION_SECRET = os.getenv("SESSION_SECRET", "some_session_secret")

app = FastAPI()
# Use defaults for SessionMiddleware, no secure/samesite arguments
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/health")
def health_check():
    return {"status":"ok"}
