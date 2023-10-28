from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
usuarios= []
# Modelo usuarios 
class Usuario(BaseModel):
      Nombre : str 
      Numero: int 
@app.get('/')
def root():
    return {"welcome": "Hello, world"}
@app.get('/usuarios')
def mostrar_usuarios():
    return usuarios 
@app.post('/usuarios')
def registro (Datos : Usuario):
    usuarios.append(dict(Datos))
    return "Recivido"
