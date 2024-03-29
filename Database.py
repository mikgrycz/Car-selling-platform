from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI
from dotenv import load_dotenv
import os
# for msql
import mysql.connector



load_dotenv() 
mysql_password = os.getenv('MYSQL_PASSWORD')
URL_DATABASE = 'mysql+pymysql://root:' + mysql_password + '@localhost:3306/cartradingsystem'

engine = create_engine(URL_DATABASE, pool_timeout=60)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from dotenv import load_dotenv, find_dotenv

load_dotenv()
