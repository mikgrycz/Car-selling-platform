from User import User
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from Database import Base
from pydantic import BaseModel

class Message(Base):
    __tablename__ = 'messages'

    MessageID = Column(Integer, primary_key=True)
    Sender = Column(String(255))
    Recipient = Column(String(255))
    Content = Column(String(255))
    TimeStamp = Column(DateTime, default=datetime.now)

    def SendMessage(self):
        print("Send Message")

    def ReceiveMessage(self):
        print("Receive Message")

    def DeleteMessage(self):
        print("Delete Message")
class MessageModel(BaseModel):
    MessageID: int
    Sender: str
    Recipient: str
    Content: str
    TimeStamp: datetime