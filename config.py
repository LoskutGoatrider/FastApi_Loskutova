from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class DBSettings():
    @staticmethod
    def get_session():
        server = "DESKTOP-PCTNAG1\\SQLEXPRESS"
        database = "testtest"
        engine = create_engine(f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes")
        return Session(bind=engine)


