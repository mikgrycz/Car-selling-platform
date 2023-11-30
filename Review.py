from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from User import User
from Car import Car
from sqlalchemy.ext.declarative import declarative_base
from Database import Base

class Review(Base):
    __tablename__ = 'reviews'
    ReviewID = Column(Integer, primary_key=True)
    Rating = Column(Integer)
    Comment = Column(String(255))
    ReviewerID = Column(Integer, ForeignKey('Users.UserID'))
    Reviewer = relationship("User")
    CarSoldID = Column(Integer, ForeignKey('cars.CarID'))
    CarSold = relationship("Car")

    def AddReview(self):
        print("Add Review")

    def EditReview(self):
        print("Edit Review")

    def DeleteReview(self):
        print("Delete Review")