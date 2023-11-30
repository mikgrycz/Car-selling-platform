from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from Database import Base

class User(Base):
    __tablename__ = 'Users'

    UserID = Column(Integer, primary_key=True)
    UserName = Column(String(255))
    UserPassword = Column(String(255))
    UserEmail = Column(String(255))
    UserPhone = Column(String(255))
    FirstName = Column(String(255))
    LastName = Column(String(255))

    def set(self, UserID, UserName, UserPassword, UserEmail, UserPhone, FirstName, LastName):
        self.UserID = UserID
        self.UserName = UserName
        self.UserPassword = UserPassword
        self.UserEmail = UserEmail
        self.UserPhone = UserPhone
        self.FirstName = FirstName
        self.LastName = LastName

    def login(self):
        print("Login")

    def logout(self):
        print("Logout")

    def searchCars(query):
        print("Search Cars")

    def viewCarDetails(carID):
        print("View Car Details")

    def contactSeller(carID):
        print("Contact Seller")

# engine = create_engine('sqlite:///database.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
