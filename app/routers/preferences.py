from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional, List
from app.db import get_session
from app.models.user_preferences import UserPreferences
from app.models.user import User
from app.utils.auth_utils import get_current_user
from pydantic import BaseModel

router = APIRouter()

class PreferencesUpdate(BaseModel):
    roles: Optional[List[str]] = None
    work_arrangement: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    industries: Optional[List[str]] = None
    experience_years_min: Optional[int] = None
    experience_years_max: Optional[int] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None

@router.get("/")
def get_preferences(user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(UserPreferences).where(UserPreferences.user_id == user.id)
    prefs = session.exec(statement).one_or_none()
    if prefs is None:
        return {}  # No preferences set yet.
    # Return full model data without exclude_unset, ensuring all fields appear.
    return prefs.model_dump()

@router.post("/")
def set_preferences(
    prefs_data: PreferencesUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(UserPreferences).where(UserPreferences.user_id == user.id)
    prefs = session.exec(statement).one_or_none()

    if prefs is None:
        prefs = UserPreferences(user_id=user.id)
        session.add(prefs)

    # Update fields only if provided
    if prefs_data.roles is not None:
        prefs.roles = prefs_data.roles
    if prefs_data.work_arrangement is not None:
        prefs.work_arrangement = prefs_data.work_arrangement
    if prefs_data.country is not None:
        prefs.country = prefs_data.country
    if prefs_data.state is not None:
        prefs.state = prefs_data.state
    if prefs_data.city is not None:
        prefs.city = prefs_data.city
    if prefs_data.industries is not None:
        prefs.industries = prefs_data.industries
    if prefs_data.experience_years_min is not None:
        prefs.experience_years_min = prefs_data.experience_years_min
    if prefs_data.experience_years_max is not None:
        prefs.experience_years_max = prefs_data.experience_years_max
    if prefs_data.salary_min is not None:
        prefs.salary_min = prefs_data.salary_min
    if prefs_data.salary_max is not None:
        prefs.salary_max = prefs_data.salary_max

    session.commit()
    session.refresh(prefs)
    # Return full data after setting preferences
    return prefs.model_dump()
