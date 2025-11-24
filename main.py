from sqlmodel import  SQLModel
from models.engine import engine
from menu import menu

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

   
menu()