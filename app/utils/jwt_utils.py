import os
from jose import jwt
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET", "secret")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def create_jwt(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

def verify_jwt(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
