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
    load_dotenv()
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv('mysql')
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS CarTradingSystem")
    mycursor.execute("USE CarTradingSystem")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Car (CarID INT AUTO_INCREMENT PRIMARY KEY, Brand VARCHAR(255), Model VARCHAR(255), Year INT, Mileage INT, Color VARCHAR(255), Price INT, Description VARCHAR(255))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Client (ClientID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Review (ReviewID INT AUTO_INCREMENT PRIMARY KEY, Rating INT, Comment VARCHAR(255), ReviewerID INT, CarID INT)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Message (MessageID INT AUTO_INCREMENT PRIMARY KEY, SenderID INT, ReceipientID INT, Content VARCHAR(255), TimeStamp DATETIME)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Transaction (TransactionID INT AUTO_INCREMENT PRIMARY KEY, BuyerID INT, SellerID INT, CarID INT, Price INT, TimeStamp DATETIME)")
    mycursor.execute("CREATE TABLE IF NOT EXISTS SuperUser (SuperUserID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Email VARCHAR(255), Password VARCHAR(255))")
    print("Welcome to Car Trading System!")
    print("Please login to continue")
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()
    print("Logging in...")
