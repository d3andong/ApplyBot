import os
from sqlmodel import SQLModel, create_engine, Session

# Import models so SQLModel knows about them when creating tables
from app.models.user import User
from app.models.user_preferences import UserPreferences
# If you have other models like Resume or Jobs, import them here as well

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://devuser:devpass@localhost:5432/jobapp")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    # Creates the tables for all SQLModel models discovered (User, UserPreferences, etc.)
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
