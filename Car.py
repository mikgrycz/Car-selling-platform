from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from Database import Base
from pydantic import BaseModel
from typing import Optional
import os
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
    PictureLink = Column(String(255))
    BodyType = Column(String(255))
    NumberOfReviews = Column(Integer)

    def GetCarDetails(self):
        print("CarID: " + str(self.CarID) + "\nMake: " + self.Make + "\nModel: " + self.Model + "\nYear: " + str(self.Year) + "\nPrice: " + str(self.Price) + "\nMileage: " + str(self.Mileage) + "\nDescription: " + self.Description + "\nSellerID: " + str(self.SellerID) + "\n")

    def SetCarDetails(self, CarID, Make, Model, Year, Price, Mileage, Description, SellerID, BodyType):
        self.CarID = CarID
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Mileage = Mileage
        self.Description = Description
        self.SellerID = SellerID
        self.PictureLink = "../CarData/c" + str(CarID) + "/1.png"
        self.BodyType = BodyType

    # def __init__(self, CarID, Make, Model, Year, Price, Mileage, Description, SellerID, BodyType):
    #     # create new folder for car images c + carID in CarData
    #     self.SetCarDetails(CarID, Make, Model, Year, Price, Mileage, Description, SellerID, BodyType)
    #     folder_name = f"c{CarID}"
    #     folder_path = os.path.join("CarData", folder_name)
    #     os.makedirs(folder_path)

    # def __init__(self):
    #     pass
    # create new folder for car images c + carID in CarData
        #folder_name = f"c000001"  #placeholder
        #folder_path = os.path.join("CarData", folder_name)
        #os.makedirs(folder_path)


class CarModel(BaseModel):
    CarID: Optional[int] = None
    Make: str
    Model: str
    Year: int
    Price: int
    Mileage: int
    Description: str
    SellerID: int
    PictureLink: str
    BodyType: str
