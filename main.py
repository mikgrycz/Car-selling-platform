from Car import Car
from User import User
from Message import Message
from Review import Review
from Transaction import Transaction, RealTransaction, ProxyTransaction
from SuperUser import SuperUser
from datetime import datetime
import mysql.connector
import os
from os.path import join, dirname
import sys
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from Database import SessionLocal, engine
import Models
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
Models.Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
Models.Base.metadata.create_all(bind=engine)


#import .env file variables
from dotenv import load_dotenv, find_dotenv
if __name__ == "__main__":
    print("Initiating...")

# Define endpoints for each class

@app.get("/cars")
def get_cars(db: Session = Depends(get_db)):
    cars = db.query(Car).all()
    return cars

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return messages

@app.get("/reviews")
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(Review).all()
    return reviews

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@app.get("/superusers")
def get_superusers(db: Session = Depends(get_db)):
    superusers = db.query(SuperUser).all()
    return superusers

# @app.post("/users")
# def create_user(user: UserModel, db: Session = Depends(get_db)):
#     db_user = User(**user.model_dump())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.post("/users")
# def add_user(user: User, db: Session = Depends(get_db)):
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

