from sqlmodel import Field, SQLModel, create_engine, Session, select
from models.agents import Agents
from models.reports import Reports, add_report
from models.terorists import Terorists
from models.engine import engine
from function import *


def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Create report")
        print("2. Delete report")
        print("3. Search report by ID")
        print("4. Search report by word")
        print("5. Show all reports")
        print("0. Exit")
        
        choice = input("enter your choice")
        
        if choice == "1":
            add_report()
        elif choice == "2":
            delete_report()
        elif choice == "3":
            search_report()
        elif choice == "4":
            search_report_word()
        elif choice == "5":
            get_reports()
        elif choice == "0":
            print("end!")
            break
        else:
            print("invalid choice")