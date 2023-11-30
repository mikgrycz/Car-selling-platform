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

engine = create_engine(URL_DATABASE)
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
# mydb = mysql.connector.connect(
# host = "localhost",
# User = "root",
# password = os.getenv('MYSQL_PASSWORD')
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

# # ALTER TABLE statements to modify existing tables if necessary
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Brand VARCHAR(255)")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Model VARCHAR(255)")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Year INT")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Mileage INT")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Color VARCHAR(255)")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Price INT")
# mycursor.execute("ALTER TABLE Car MODIFY COLUMN Description VARCHAR(255)")

# mycursor.execute("ALTER TABLE User MODIFY COLUMN Name VARCHAR(255)")
# mycursor.execute("ALTER TABLE User MODIFY COLUMN Email VARCHAR(255)")
# mycursor.execute("ALTER TABLE User MODIFY COLUMN Password VARCHAR(255)")

# mycursor.execute("ALTER TABLE Review MODIFY COLUMN Rating INT")
# mycursor.execute("ALTER TABLE Review MODIFY COLUMN Comment VARCHAR(255)")
# mycursor.execute("ALTER TABLE Review MODIFY COLUMN ReviewerID INT")
# mycursor.execute("ALTER TABLE Review MODIFY COLUMN CarID INT")

# mycursor.execute("ALTER TABLE Message MODIFY COLUMN SenderID INT")
# mycursor.execute("ALTER TABLE Message MODIFY COLUMN ReceipientID INT")
# mycursor.execute("ALTER TABLE Message MODIFY COLUMN Content VARCHAR(255)")
# mycursor.execute("ALTER TABLE Message MODIFY COLUMN TimeStamp DATETIME")

# mycursor.execute("ALTER TABLE Transaction MODIFY COLUMN BuyerID INT")
# mycursor.execute("ALTER TABLE Transaction MODIFY COLUMN SellerID INT")
# mycursor.execute("ALTER TABLE Transaction MODIFY COLUMN CarID INT")
# mycursor.execute("ALTER TABLE Transaction MODIFY COLUMN Price INT")
# mycursor.execute("ALTER TABLE Transaction MODIFY COLUMN TimeStamp DATETIME")

# mycursor.execute("ALTER TABLE SuperUser MODIFY COLUMN Name VARCHAR(255)")
# mycursor.execute("ALTER TABLE SuperUser MODIFY COLUMN Email VARCHAR(255)")
# mycursor.execute("ALTER TABLE SuperUser MODIFY COLUMN Password VARCHAR(255)")

# print("Welcome to Car Trading System!")
# mycursor.close()
