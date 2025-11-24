from sqlmodel import Field, SQLModel, create_engine, Session, select
from engine import engine


class Agents(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    password: str
    
def add_agent(name: str, password: str):
    agent = Agents(name=name, password=password)
    with Session(engine) as session:
        session.add(agent)
        session.commit()
        session.refresh(agent)
        print(f"added agent with id={agent.id}")
        
def get_agents() -> list[Agents]:
    with Session(engine) as session:
        statemant = select(Agents())
        result = session.exec(statemant)
        agents = result.all()
        return agents
    
