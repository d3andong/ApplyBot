from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import os
from app.routers import auth, preferences

SESSION_SECRET = os.getenv("SESSION_SECRET", "some_session_secret")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(preferences.router, prefix="/preferences", tags=["preferences"])

@app.get("/health")
def health_check():
    return {"status":"ok"}
