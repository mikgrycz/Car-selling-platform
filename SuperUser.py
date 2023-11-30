# singleton class for super User
from User import User
from Car import Car
from Database import Base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from pydantic import BaseModel
class SuperUser(User):   #### SINGLETON #####
    __instance = None
    __tablename__ = 'superuser'
    id = Column(Integer, ForeignKey('users.UserID'), primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))

    @staticmethod
    def getInstance():
        """ Static access method. """
        if SuperUser.__instance == None:
            SuperUser()
        return SuperUser.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if SuperUser.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SuperUser.__instance = self
            self.name = "SuperUser"
            self.password = "SuperUser"
            self.email = "support@shop.com"
            self.engine = create_engine('sqlite:///database.db')
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

    def ListCarForSale(self):
        print("List Car For Sale")

    def RemoveCarFromSale(self):
        print("Remove Car From Sale")

    def EditCarListing(self):
        print("Edit Car Details")

    def ViewUserProfile(UserID):
        print("View User Profile")
class SuperUserModel(BaseModel):
    id: int
    name: str
    password: str
    email: str

    class Config:
        orm_mode = True
