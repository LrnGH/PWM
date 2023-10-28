from pydantic import BaseModel

# Modelo usuarios 
class Usuario(BaseModel):
      nombre: str 
      numero: int