from typing import List, Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB

class UserPreferences(SQLModel, table=True):
    user_id: int = Field(primary_key=True, foreign_key="user.id")
    roles: List[str] = Field(default_factory=list, sa_column=Column(JSONB))
    work_arrangement: str = Field(default="hybrid")
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    industries: List[str] = Field(default_factory=list, sa_column=Column(JSONB))
    experience_years_min: Optional[int] = None
    experience_years_max: Optional[int] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
