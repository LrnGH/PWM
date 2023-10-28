from fastapi import FastAPI
from models import Usuario

app = FastAPI()
usuarios= []

#TODO: documentar los endpoints de tal manera que se vean en swagger 
# Aprender los verbos HTTP (GET, POST, PUT, DELETE)
# Pasar toda el app a ingles

@app.get('/')
def root():
    return {"welcome": "Hello, world"}

@app.get('/usuarios')
def get_users():
    return {"usuarios": usuarios}  

@app.post('/usuarios')
def post_user (Datos : Usuario):
    usuarios.append(dict(Datos))
    return {"mensaje":"Recibido"}
