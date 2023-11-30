from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from Database import Base
from pydantic import BaseModel

class Car(Base):
    __tablename__ = 'cars'
    CarID = Column(Integer, primary_key=True)
    Make = Column(String(255))
    Model = Column(String(255))
    Year = Column(Integer)
    Price = Column(Integer)
    Mileage = Column(Integer)
    Description = Column(String(255))
    SellerID = Column(Integer)

    def GetCarDetails(self):
        print("CarID: " + str(self.CarID) + "\nMake: " + self.Make + "\nModel: " + self.Model + "\nYear: " + str(self.Year) + "\nPrice: " + str(self.Price) + "\nMileage: " + str(self.Mileage) + "\nDescription: " + self.Description + "\nSellerID: " + str(self.SellerID) + "\n")

    def SetCarDetails(self, CarID, Make, Model, Year, Price, Mileage, Description, SellerID):
        self.CarID = CarID
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Mileage = Mileage
        self.Description = Description
        self.SellerID = SellerID

class CarModel(BaseModel):
    CarID: int
    Make: str
    Model: str
    Year: int
    Price: int
    Mileage: int
    Description: str
    SellerID: int
