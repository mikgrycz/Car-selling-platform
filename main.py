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
import Models
from Database import SessionLocal, engine
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
# @app.post("/posts/", status_code=status.HTTP_201_CREATED)
# async def create_post(post: PostBase, db: db_dependency):
#     db_post = Models.Post(**post.model_dump())
#     db.add(db_post)
#     db.commit()

# @app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def get_post(post_id: int, db: db_dependency):
#     db_post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return db_post

# @app.post("/Users/", status_code=status.HTTP_201_CREATED)
# async def create_User(User: UserBase, db: db_dependency):
#     db_User = Models.User(**User.model_dump())
#     db.add(db_User)
#     db.commit()

# @app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency):
#     db_post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
#     if db_post is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
#     db.delete(db_post)
#     db.commit()

# @app.get("/Users/{User_id}", status_code=status.HTTP_200_OK)
# async def get_User(User_id: int, db: db_dependency):
#     db_User = db.query(Models.User).filter(Models.User.id == User_id).first()
#     if db_User is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
#     return db_User

# @app.get("/Users/", status_code=status.HTTP_200_OK)
# async def get_Users(db: db_dependency):
#     db_Users = db.query(Models.User).all()
#     return db_Users

# @app.post("/cars/", status_code=status.HTTP_201_CREATED)
# async def create_car(car: Car):
    
#     pass

# @app.get("/cars/{car_id}", status_code=status.HTTP_200_OK)
# async def get_car(car_id: int):
#     # Code to get a car by ID
#     pass

# @app.put("/cars/{car_id}", status_code=status.HTTP_200_OK)
# async def update_car(car_id: int, car: Car):
#     # Code to update a car by ID
#     pass

# @app.delete("/cars/{car_id}", status_code=status.HTTP_200_OK)
# async def delete_car(car_id: int):
#     # Code to delete a car by ID
#     pass

# @app.post("/Users/", status_code=status.HTTP_201_CREATED)
# async def create_User(User: User):
#     # Code to create a User
#     pass

# @app.get("/Users/{User_id}", status_code=status.HTTP_200_OK)
# async def get_User(User_id: int):
#     # Code to get a User by ID
#     pass

# @app.put("/Users/{User_id}", status_code=status.HTTP_200_OK)
# async def update_User(User_id: int, User: User):
#     # Code to update a User by ID
#     pass

# @app.delete("/Users/{User_id}", status_code=status.HTTP_200_OK)
# async def delete_User(User_id: int):
#     # Code to delete a User by ID
#     pass

# @app.post("/messages/", status_code=status.HTTP_201_CREATED)
# async def create_message(message: Message):
#     # Code to create a message
#     pass

# @app.get("/messages/{message_id}", status_code=status.HTTP_200_OK)
# async def get_message(message_id: int):
#     # Code to get a message by ID
#     pass

# @app.put("/messages/{message_id}", status_code=status.HTTP_200_OK)
# async def update_message(message_id: int, message: Message):
#     # Code to update a message by ID
#     pass

# @app.delete("/messages/{message_id}", status_code=status.HTTP_200_OK)
# async def delete_message(message_id: int):
#     # Code to delete a message by ID
#     pass

# @app.post("/reviews/", status_code=status.HTTP_201_CREATED)
# async def create_review(review: Review):
#     # Code to create a review
#     pass

# @app.get("/reviews/{review_id}", status_code=status.HTTP_200_OK)
# async def get_review(review_id: int):
#     # Code to get a review by ID
#     pass

# @app.put("/reviews/{review_id}", status_code=status.HTTP_200_OK)
# async def update_review(review_id: int, review: Review):
#     # Code to update a review by ID
#     pass

# @app.delete("/reviews/{review_id}", status_code=status.HTTP_200_OK)
# async def delete_review(review_id: int):
#     # Code to delete a review by ID
#     pass

# @app.post("/transactions/", status_code=status.HTTP_201_CREATED)
# async def create_transaction(transaction: Transaction):
#     # Code to create a transaction
#     pass

# @app.get("/transactions/{transaction_id}", status_code=status.HTTP_200_OK)
# async def get_transaction(transaction_id: int):
#     # Code to get a transaction by ID
#     pass

# @app.put("/transactions/{transaction_id}", status_code=status.HTTP_200_OK)
# async def update_transaction(transaction_id: int, transaction: Transaction):
#     # Code to update a transaction by ID
#     pass

# @app.delete("/transactions/{transaction_id}", status_code=status.HTTP_200_OK)
# async def delete_transaction(transaction_id: int):
#     # Code to delete a transaction by ID
#     pass

# @app.post("/superUsers/", status_code=status.HTTP_201_CREATED)
# async def create_superUser(superUser: SuperUser):
#     # Code to create a superUser
#     pass

# @app.get("/superUsers/{superUser_id}", status_code=status.HTTP_200_OK)
# async def get_superUser(superUser_id: int):
#     # Code to get a superUser by ID
#     pass

# @app.put("/superUsers/{superUser_id}", status_code=status.HTTP_200_OK)
# async def update_superUser(superUser_id: int, superUser: SuperUser):
#     # Code to update a superUser by ID
#     pass

# @app.delete("/superUsers/{superUser_id}", status_code=status.HTTP_200_OK)
# async def delete_superUser(superUser_id: int):
#     # Code to delete a superUser by ID
#     pass


#import .env file variables
from dotenv import load_dotenv, find_dotenv
if __name__ == "__main__":
    print("Initiating...")
    # load_dotenv()
    # mydb = mysql.connector.connect(
    # host = "localhost",
    # User = "root",
    # password = os.getenv('mysql')
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS CarTradingSystem")
    # mycursor.execute("USE CarTradingSystem")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Car (CarID INT AUTO_INCREMENT PRIMARY KEY, Brand VARCHAR(255), Model VARCHAR(255), Year INT, Mileage INT, Color VARCHAR(255), Price INT, Description VARCHAR(255))")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS User (UserID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Review (ReviewID INT AUTO_INCREMENT PRIMARY KEY, Rating INT, Comment VARCHAR(255), ReviewerID INT, CarID INT)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Message (MessageID INT AUTO_INCREMENT PRIMARY KEY, SenderID INT, ReceipientID INT, Content VARCHAR(255), TimeStamp DATETIME)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Transaction (TransactionID INT AUTO_INCREMENT PRIMARY KEY, BuyerID INT, SellerID INT, CarID INT, Price INT, TimeStamp DATETIME)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS SuperUser (SuperUserID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    # print("Welcome to Car Trading System!")
    # print("Please login to continue")
    # print("Username: ")
    # Username = input()
    # print("Password: ")
    # password = input()
    # print("Logging in...")
    # mycursor.close()
