from fastapi import APIRouter, Request, Response, Depends
from starlette.responses import RedirectResponse
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth
import os

from app.db import get_session
from sqlmodel import select, Session
from app.models.user import User
from app.utils.jwt_utils import create_jwt
from app.utils import get_current_user
from app.config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET


router = APIRouter()

config = Config(".env")
oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@router.get("/google")
async def google_login(request: Request):
    # Just print the session to ensure it's accessible
    print("Session before redirect:", request.session)
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(request: Request, response: Response, session: Session = Depends(get_session)):
    # Debugging print
    print("Session at callback:", request.session)
    token = await oauth.google.authorize_access_token(request)
    userinfo = token['userinfo']
    statement = select(User).where(User.google_id == userinfo['sub'])
    user = session.exec(statement).one_or_none()
    if not user:
        user = User(google_id=userinfo['sub'], email=userinfo['email'], name=userinfo.get('name','No Name'))
        session.add(user)
        session.commit()
        session.refresh(user)

    jwt_token = create_jwt({"id": user.id})
    # Redirect to a protected endpoint or /auth/me
    resp = RedirectResponse(url="/auth/me")
    resp.set_cookie("token", jwt_token, httponly=True, samesite='lax') # keep defaults simple
    return resp

@router.get("/me")
async def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "email": user.email, "name": user.name}


print("GOOGLE_CLIENT_ID:", os.getenv("GOOGLE_CLIENT_ID"))
print("GOOGLE_CLIENT_SECRET:", os.getenv("GOOGLE_CLIENT_SECRET"))
