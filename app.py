import uvicorn 
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import os
from schemas import User as schemamodel 
from schemas import update
from models import Users_table as modeluser 
from fastapi_sqlalchemy import db 
from fastapi_sqlalchemy import DBSessionMiddleware


load_dotenv(".env")


app= FastAPI(debug=True)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get('/', description="root")
def root(): 
    return {"Message":"Helo, World"}


# Add a new user in the dabase 
@app.post('/add_user/', response_model=schemamodel) 
def add_user (New_user: schemamodel):
    db_user =  modeluser(name =New_user.name, number=New_user.number)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user

# show all the users in the database 
@app.get('/users')
def get_users():
    Users=db.session.query(modeluser).all()
    return Users 


# Search for a user by name
@app.get('/get_user')
def get_user(name: str):  
    record= db.session.query(modeluser).filter(modeluser.name==name).first()
    if record is None: 
        raise  HTTPException(status_code=404, detail="User not found")
    else:
        return record 
   
# Update user 
@app.put("/update_user/{name}")
def update_user(New_info:update):
    db_user= db.session.query(modeluser).filter(modeluser.name==New_info.user_name).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else: 
        db_user.name = New_info.New_name
        db_user.number = New_info.New_number
        db.session.commit()
        db.session.refresh(db_user)
        return {"update":"The user has been update", 
                  "name": db_user.name,
                   "number": db_user.number }
        

#Delete user 
@app.delete('/delete/{name}')
def delete_user(name:str):
    db_user= db.session.query(modeluser).filter(modeluser.name==name).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else: 
        db.session.delete(db_user)
        db.session.commit()
        return {"Success":"The user was deleted"}
    
