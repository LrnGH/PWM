from pydantic import BaseModel 
from typing import Optional

class User(BaseModel):
    name: str 
    number: str

    class Config:
        orm_mode = True
class update(BaseModel):
    user_name: str
    New_name: str 
    New_number: str 

class message(BaseModel):
    Header: Optional[str]
    Message: str 
    Image: Optional[str]

