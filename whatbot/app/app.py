#TODO: documentar los endpoints de tal manera que se vean en swagger 
# Aprender los verbos HTTP (GET, POST, PUT, DELETE)
# Pasar toda el app a ingles


from fastapi import FastAPI, Depends 
from schemas import user
from sqlalchemy.orm import Session
from db import get_db 
from model import User_Table 

app = FastAPI(debug=True)


@app.get('/')
def root():
    return {"welcome": "Hello"}

@app.post('/users')
def create(details: user, db: Session = Depends(get_db)):
    to_create = User_Table(name =details.name, 
                           number=details.number)
    db.add(to_create)
    db.commit()
    return { "success": True,
            "created_id": to_create.id }  
@app.get('/users')
def get_by_name(name: str, db: Session = Depends(get_db)):
    return db.query(User_Table).filter(User_Table.name==name).first()
    