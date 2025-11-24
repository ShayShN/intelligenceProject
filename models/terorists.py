from sqlmodel import Field, SQLModel, create_engine, Session, select
from engine import engine


class Terorists(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    
def add_terorist(name: str):
    terorist = Terorists(name=name)   
    with Session(engine) as session:
        session.add(terorist)
        session.commit()
        session.refresh(terorist)
        print(f"added terorist with id={terorist.id}")

def get_terorists() -> list[Terorists]:
    with Session(engine) as session:
        statemant = select(Terorists)
        result = session.exec(statemant)
        terorists = result.all()
        return terorists
    
# add_terorist("Mochamad")
# add_terorist("Yaser")