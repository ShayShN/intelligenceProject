from sqlmodel import create_engine

url_database = "mysql+mysqlconnector://root@localhost:3306/intelligence?use_pure=true"
engine = create_engine(url_database, echo=True)