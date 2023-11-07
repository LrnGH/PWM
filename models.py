from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base= declarative_base ()

class Users_table(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)
     
    def __init__(self, name, number):
        self.name = name
        self.number = number

    