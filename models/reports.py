from sqlmodel import Field, SQLModel, create_engine, Session, select
from models import terorists
from engine import engine


class Reports(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    id_agent: int = Field(default=None, foreign_key="agents.id")
    id_terorist: int = Field(default=None, foreign_key="terorists.id")
    date: str
    category: str
    detail: str



