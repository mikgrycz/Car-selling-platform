from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Database import Base
from User import User
from Car import Car
#from pydantic import BaseModel
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    sender = Column(String(255))
    receiver = Column(String(255))
    amount = Column(Integer)

    def InitiateTransaction(self) -> None:
        pass

    def CompleteTransaction(self):
        pass

    def CancelTransaction(self):
        pass

class RealTransaction(Transaction):
    TransactionID = 0
    buyer = User()
    seller = User()
    car = Car()
    date = ""
    status = ""

    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def InitiateTransaction(self):
        print("Initiate Transaction")

    def CompleteTransaction(self):
        print("Complete Transaction")

    def CancelTransaction(self):
        print("Cancel Transaction")

class ProxyTransaction(Transaction):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def InitiateTransaction(self):
        self.realTransaction = RealTransaction(self.sender, self.receiver, self.amount)
        self.realTransaction.InitiateTransaction()

    def CompleteTransaction(self):
        if self.IsAuthorized():
            self.realTransaction.CompleteTransaction()
        else:
            print("Not Authorized to Complete Transaction")

    def CancelTransaction(self):
        if self.IsAuthorized():
            self.realTransaction.CancelTransaction()
        else:
            print("Not Authorized to Cancel Transaction")

    def IsAuthorized(self):
        return self.sender == "SuperUser"

# Create the database engine
# engine = create_engine('sqlite:///transactions.db', echo=True)

# # Create the tables
# Base.metadata.create_all(bind=engine)

# # Create a session
# Session = sessionmaker(bind=engine)
# session = Session()
# class TransactionModel(BaseModel):
#     id: int
#     sender: str
#     receiver: str
#     amount: int

# class RealTransactionModel(TransactionModel):
#     TransactionID: int
#     buyer: User
#     seller: User
#     car: Car
#     date: str
#     status: str
# class ProxyTransactionModel(TransactionModel):
#     pass
