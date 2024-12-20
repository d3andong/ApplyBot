from fastapi import Depends, HTTPException, status, Request
from app.utils.jwt_utils import verify_jwt
from app.db import get_session
from sqlmodel import select, Session
from app.models.user import User

async def get_current_user(request: Request, session: Session = Depends(get_session)) -> User:
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = verify_jwt(token)
        user_id: int = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one_or_none()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
