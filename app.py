import uvicorn 
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import os
import json
from schemas import User as schemamodel 
from schemas import update, message
from models import Users_table as modeluser 
from models import Message_table
from fastapi_sqlalchemy import db 
from fastapi_sqlalchemy import DBSessionMiddleware
from whatsapp import get_text_message_input, send_message
from prompt import create_message
 



load_dotenv(".env")

app= FastAPI(debug=True)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get('/', description="root")
def root(): 
    return {"Message":"Helo, World"}


# Add a new user in the dabase 
@app.post('/add_user/', response_model=schemamodel, description="Add a new user in the dabase") 
def add_user (New_user: schemamodel):
    db_user =  modeluser(name =New_user.name, number=New_user.number)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user

# show all the users in the database 
@app.get('/users', description="show all the users in the database")
def get_users():
    Users=db.session.query(modeluser).all()
    return Users 


# Search for a user by name
@app.get('/get_user', description="Search for a user by name")
def get_user(name: str):  
    record= db.session.query(modeluser).filter(modeluser.name==name).first()
    if record is None: 
        raise  HTTPException(status_code=404, detail="User not found")
    else:
        return record 
   
# Update user 
@app.put("/update_user/{name}", description="Update user: allow change the name and/or number")
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
@app.delete('/delete/{name}', description="Delete user by name")
def delete_user(name:str):
    db_user= db.session.query(modeluser).filter(modeluser.name==name).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else: 
        db.session.delete(db_user)
        db.session.commit()
        return {"Success":"The user was deleted"}

#send a message 
@app.post("/send_message/")
async def send_message_route(recipient: str, prompt: str):
    message=create_message(prompt)
    data = get_text_message_input(recipient, message)
    result = await send_message(json.dumps(data))
    return {"message": f"The next message has been send:{message} ", "response": result}

 


