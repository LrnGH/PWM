from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from db import Base

class User(Base): 
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(Integer, nullable=False)