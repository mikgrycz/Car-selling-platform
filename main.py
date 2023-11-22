from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import Models
from Database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base

app = FastAPI()
Models.Base.metadata.create_all(bind=engine)
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Car(Base):
    __tablename__ = "Car"
    CarID = Column(Integer, primary_key=True, index=True)
    Brand = Column(String(255))
    Model = Column(String(255))
    Year = Column(Integer)
    Mileage = Column(Integer)
    Color = Column(String(255))
    Price = Column(Integer)
    Description = Column(String(255))
    reviews = relationship("Review", back_populates="car")
    transactions = relationship("Transaction", back_populates="car")


class Client(Base):
    __tablename__ = "Client"
    ClientID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Password = Column(String(255))
    reviews = relationship("Review", back_populates="client")
    messages = relationship("Message", back_populates="client")
    transactions = relationship("Transaction", back_populates="client")

class Review(Base):
    __tablename__ = "Review"
    ReviewID = Column(Integer, primary_key=True, index=True)
    Rating = Column(Integer)
    Comment = Column(String(255))
    CarID = Column(Integer, ForeignKey('Car.CarID'))
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    car = relationship("Car", back_populates="reviews")
    client = relationship("Client", back_populates="reviews")

class Message(Base):
    __tablename__ = "Message"
    MessageID = Column(Integer, primary_key=True, index=True)
    Content = Column(String(255))
    Date = Column(DateTime)
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    client = relationship("Client", back_populates="messages")

class Transaction(Base):
    __tablename__ = "Transaction"
    TransactionID = Column(Integer, primary_key=True, index=True)
    Date = Column(DateTime)
    CarID = Column(Integer, ForeignKey('Car.CarID'))
    ClientID = Column(Integer, ForeignKey('Client.ClientID'))
    car = relationship("Car", back_populates="transactions")
    client = relationship("Client", back_populates="transactions")

class SuperUser(Base):
    __tablename__ = "SuperUser"
    SuperUserID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Password = Column(String(255))

db_dependency = Annotated[Session, Depends(get_db)]
@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = Models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def get_post(post_id: int, db: db_dependency):
    db_post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_post

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = Models.User(**user.model_dump())
    db.add(db_user)
    db.commit()

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(db_post)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    db_user = db.query(Models.User).filter(Models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return db_user

from Car import Car
from Client import Client
from Message import Message
from Review import Review
from Transaction import Transaction
from SuperUser import SuperUser
from datetime import datetime
import mysql.connector
import os
from os.path import join, dirname
import sys
#import .env file variables
from dotenv import load_dotenv, find_dotenv
if __name__ == "__main__":
    print("Initiating...")
    # load_dotenv()
    # mydb = mysql.connector.connect(
    # host = "localhost",
    # user = "root",
    # password = os.getenv('mysql')
    # )
    # mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE IF NOT EXISTS CarTradingSystem")
    # mycursor.execute("USE CarTradingSystem")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Car (CarID INT AUTO_INCREMENT PRIMARY KEY, Brand VARCHAR(255), Model VARCHAR(255), Year INT, Mileage INT, Color VARCHAR(255), Price INT, Description VARCHAR(255))")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Client (ClientID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Review (ReviewID INT AUTO_INCREMENT PRIMARY KEY, Rating INT, Comment VARCHAR(255), ReviewerID INT, CarID INT)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Message (MessageID INT AUTO_INCREMENT PRIMARY KEY, SenderID INT, ReceipientID INT, Content VARCHAR(255), TimeStamp DATETIME)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS Transaction (TransactionID INT AUTO_INCREMENT PRIMARY KEY, BuyerID INT, SellerID INT, CarID INT, Price INT, TimeStamp DATETIME)")
    # mycursor.execute("CREATE TABLE IF NOT EXISTS SuperUser (SuperUserID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    # print("Welcome to Car Trading System!")
    # print("Please login to continue")
    # print("Username: ")
    # username = input()
    # print("Password: ")
    # password = input()
    # print("Logging in...")
    # mycursor.close()
