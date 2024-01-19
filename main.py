from Car import Car, CarModel
from User import User, UserModel
from Message import Message, MessageModel
from Review import Review, ReviewModel
from Transaction import Transaction, TransactionModel
from SuperUser import SuperUser, SuperUserModel
from datetime import datetime
import mysql.connector
import os
from os import makedirs
from os.path import join, dirname
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
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
app = FastAPI()
Models.Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = get_user_from_token(token)  # You'll need to implement this function
    if not user:
        raise HTTPException(
            status_code=401, 
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password"
#         )
#     # generate JWT token
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

@app.get("/cars")
def get_cars(db: Session = Depends(get_db)):
    db = SessionLocal()
    cars = db.query(Car).all()
    return {"cars": [car.__dict__ for car in cars]}

@app.get("/car/{car_id}")
def get_car(car_id: str):
    db = SessionLocal()
    car = db.query(Car).filter(Car.CarID == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car
class LoginData(BaseModel):
    username: str
    password: str

@app.post('/api/login')
def login(data: LoginData):
    db = SessionLocal()
    user = db.query(User).filter(User.UserName == data.username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user.UserPassword != data.password:
        raise HTTPException(status_code=404, detail="Incorrect password")
    return user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.get("/messages")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).all()
    return messages

@app.get("/reviews/{car_id}")
def get_reviews(car_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.CarSoldID == car_id).all()
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

# create endpoint for 

# @app.post("/cars")
# def create_car(car: CarModel, db: Session = Depends(get_db)):
#     db_car = Car(**car.model_dump())
#     db.add(db_car)
#     db.commit()
#     db.refresh(db_car)
#     return db_car
@app.post("/messages")
def create_message(message: MessageModel, db: Session = Depends(get_db)):
    db_message = Message(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
# @app.post("/reviews")
# def create_review(review: ReviewModel, db: Session = Depends(get_db)):
#     db_review = Review(**review.dict())
#     db.add(db_review)
#     db.commit()
#     db.refresh(db_review)
#     return db_review
@app.post("/reviews")
def create_review(review: ReviewModel, db: Session = Depends(get_db)):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@app.post("/cars")
def create_car(car: CarModel, db: Session = Depends(get_db)):
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car
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


@app.post('/create-dir')
def create_dir(dir: str):
    dir_path = join('Public', 'CarData', dir)
    makedirs(dir_path, exist_ok=True)
    return { 'message': 'Directory created' }