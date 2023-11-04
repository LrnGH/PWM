# TODO: connectarse a la base de datos 
# El host de la base de datos esta corriendo en el puerto 5437:5432
# Necesitas crear las tablas (como hacer una migración usando FASTAPI.)
# El schema de la base de datos esta en el documento pero si quieres añade mas tablas
# util usar una interfaz gráfica para la base de datos como pgAdmin
# usar el ORM de FASTAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://controlio:devpassword@localhost:5437/db-ctrlio" 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db= SessionLocal()
    try: 
        yield db
    except:
        db.close()