from Car import Car, CarModel
from User import User, UserModel
from Message import Message, MessageModel
from Review import Review, ReviewModel
from Transaction import Transaction, TransactionModel
from SuperUser import SuperUser, SuperUserModel
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
from Listing import Listing, ListingModel
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security.oauth2 import OAuth2PasswordBearer
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


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate the user's credentials and return a token
    # This is just a placeholder - you'll need to implement the actual logic
    return {"access_token": "your_token", "token_type": "bearer"}

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

@app.post("/users")
def create_user(user: UserModel, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/cars")
def create_car(car: CarModel, db: Session = Depends(get_db)):
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car
@app.post("/messages")
def create_message(message: MessageModel, db: Session = Depends(get_db)):
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.post("/reviews")
def create_review(review: ReviewModel, db: Session = Depends(get_db)):
    db_review = Review(**review.model_dump())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@app.post("/transactions")
def create_transaction(transaction: TransactionModel, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.post("/superusers")
def create_superuser(superuser: SuperUserModel, db: Session = Depends(get_db)):
    db_superuser = SuperUser(**superuser.model_dump())
    db.add(db_superuser)
    db.commit()
    db.refresh(db_superuser)
    return db_superuser
@app.get("/listings")
def get_listing(listing_id:ListingModel, db: Session = Depends(get_db)):
    listing = db.query(Listing).filter(Listing.listing_id == listing_id)
    return listing
@app.post("/listings")
def create_listing(listing: ListingModel, db: Session = Depends(get_db)):
    db_listing = Listing(**listing.model_dump())
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing