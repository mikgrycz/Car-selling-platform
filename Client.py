#from Transaction import ProxyTransaction
class Client:
    UserID = 0
    UserName = ""
    UserPassword = ""
    UserEmail = ""
    UserPhone = ""
    FirstName = ""
    LastName = ""
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