from pydantic import BaseModel

# Modelo usuarios 
class user(BaseModel):
      nombre: str 
      numero: int