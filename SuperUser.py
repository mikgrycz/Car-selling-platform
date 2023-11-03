# singleton class for super user
from Client import Client
class SuperUser(Client):   #### SINGLETON #####
    __instance = None

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
            self.__name = "SuperUser"
            self.__password = "SuperUser"
            self.__email = "support@shop.com"
    def ListCarForSale(self):
        print("List Car For Sale")
    def RemoveCarFromSale(self):
        print("Remove Car From Sale")
    def EditCarListing(self):
        print("Edit Car Details")
    def ViewUserProfile(UserID):
        print("View User Profile")