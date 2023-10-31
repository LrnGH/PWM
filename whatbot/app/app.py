from fastapi import FastAPI
from whatbot.app.schemas import user

app = FastAPI()
users= []

#TODO: documentar los endpoints de tal manera que se vean en swagger 
# Aprender los verbos HTTP (GET, POST, PUT, DELETE)
# Pasar toda el app a ingles

@app.get('/')
def root():
    return {"welcome": "Hello, world"}

@app.get('/users')
def get_users():
    return {"users": users}  

@app.post('/users')
def post_user (data : user):
    users.append(dict(data))
    return {"message":" The user has been created"}
