from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from Database import Base
from pydantic import BaseModel
from Car import Car
from User import User

class Listing(Base): # Base is the declarative base from database.py  python
    __tablename__ = 'listings'
    subject_id = Column(Integer, ForeignKey('cars.CarID'))
    subject = relationship("Car")
    seller_id = Column(Integer, ForeignKey('users.UserID'))
    seller = relationship("User")
    listing_id = Column(Integer, primary_key=True)
    listing_name = Column(String(255))
    listing_description = Column(String(255))
    listing_price = Column(Integer)
    listing_location = Column(String(255))
    listing_image = Column(String(255))

    def __init__(self, listing_id, listing_name, listing_description, listing_price, listing_location, listing_image):
        self.listing_id = listing_id
        self.listing_name = listing_name
        self.listing_description = listing_description
        self.listing_price = listing_price
        self.listing_location = listing_location
        self.listing_image = listing_image

    def __str__(self):
        return f"{self.listing_id} {self.listing_name} {self.listing_description} {self.listing_price} {self.listing_location} {self.listing_image}"

    def __repr__(self):
        return f"{self.listing_id} {self.listing_name} {self.listing_description} {self.listing_price} {self.listing_location} {self.listing_image}"
    
class ListingModel(BaseModel):
    subject_id: int
    seller_id: int
    listing_id: int
    listing_name: str
    listing_description: str
    listing_price: int
    listing_location: str
    listing_image: str

    class Config:
        orm_mode = True