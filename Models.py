from sqlalchemy import Boolean, Column, Integer, String
from Database import Base, SessionLocal
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True)
    content = Column(String(100), unique=True, index=True)
    user_id = Column(Integer, index=True)
    
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
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

