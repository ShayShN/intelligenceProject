from sqlmodel import Field, SQLModel, create_engine, Session, select
from models.agents import Agents
from models.reports import Reports, add_report
from models.terorists import Terorists
from models.engine import engine


def add_report(id_agent: int, id_terorist: int, date: str, category: str, detail: str):
    report = Reports(id_agent=id_agent, id_terorist=id_terorist, date=date, category=category, detail=detail)
    with Session(engine) as session:
        session.add(report)
        session.commit()
        session.refresh(report)
        print(f"added report with id={report.id}")
        
def get_reports() -> list[Reports]:
    with Session(engine) as session:
        statemant = select(Reports)
        result = session.exec(statemant)
        reports = result.all()
        return reports
    
def delete_report():
    user_delete = int(input("what the report id to delete?: "))
    with Session(engine) as session:
        statement = select(Reports).where(Reports.id == user_delete)
        results = session.exec(statement)
        report = results.one_or_none()
        if report is None:
            print("report not found")
        print("Report: ", report)
        session.delete(report)
        session.commit()
        print("delete successfully!")
        
def search_report():
    query = int(input("enter a id report: "))
    with Session(engine) as session:
        statement = select(Reports).where(Reports.id == query)
        results = session.exec(statement).all()
        if not results:
            print("No reports found.")
        else:
            for r in results:
                print(r)

def search_report_word():
    query_word = input("enter a word to searce: ")
    with Session(engine) as session:
        statement = select(Reports).where((Reports.detail.ilike(f"%{query_word}%")) | (Reports.category.ilike(f"%{query_word}%")))
        results = session.exec(statement).all()
        if not results:
            print("No reports found.")
        else:
            for r in results:
                print(r)
                
