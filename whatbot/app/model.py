from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.schema import Column
from db import Base

class User_Table(Base): 
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    number = Column(Integer, nullable=False) 