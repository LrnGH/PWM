from pydantic import BaseModel

# Modelo usuarios 
class user(BaseModel):
      name: str 
      number: int