from django.db import models

class Car(models.Model):
    CarID = models.AutoField(primary_key=True)
    Make = models.CharField(max_length=255)
    Model = models.CharField(max_length=255)
    Year = models.IntegerField()
    Price = models.IntegerField()
    Mileage = models.IntegerField()
    Description = models.CharField(max_length=255)
    Seller = models.ForeignKey('User', on_delete=models.CASCADE)
    PictureLink = models.CharField(max_length=255)
    BodyType = models.CharField(max_length=255)
    NumberOfReviews = models.IntegerField(default=0)

    def GetCarDetails(self):
        print("CarID: " + str(self.CarID) + "\nMake: " + self.Make + "\nModel: " + self.Model + "\nYear: " + str(self.Year) + "\nPrice: " + str(self.Price) + "\nMileage: " + str(self.Mileage) + "\nDescription: " + self.Description + "\nSellerID: " + str(self.Seller.id) + "\n")

    def SetCarDetails(self, CarID, Make, Model, Year, Price, Mileage, Description, Seller, BodyType):
        self.CarID = CarID
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Price = Price
        self.Mileage = Mileage
        self.Description = Description
        self.Seller = Seller
        self.PictureLink = "../CarData/c" + str(CarID) + "/1.png"
        self.BodyType = BodyType

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=255)
    UserPassword = models.CharField(max_length=255)
    UserEmail = models.EmailField(max_length=255)
    UserPhone = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)

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

    def searchCars(self, query):
        print("Search Cars")

    def viewCarDetails(self, carID):
        print("View Car Details")

    def contactSeller(self, carID):
        print("Contact Seller")

class Transaction(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    amount = models.IntegerField()

class RealTransaction(Transaction):
    TransactionID = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def InitiateTransaction(self):
        print("Initiate Transaction")

    def CompleteTransaction(self):
        print("Complete Transaction")

    def CancelTransaction(self):
        print("Cancel Transaction")

class ProxyTransaction(Transaction):
    realTransaction = models.ForeignKey(RealTransaction, on_delete=models.CASCADE)

    def InitiateTransaction(self):
        self.realTransaction = RealTransaction.objects.create(sender=self.sender, receiver=self.receiver, amount=self.amount)
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

class SuperUser(User):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "SuperUser"
        self.password = "SuperUser"
        self.email = "support@shop.com"

    def ListCarForSale(self):
        print("List Car For Sale")

    def RemoveCarFromSale(self):
        print("Remove Car From Sale")

    def EditCarListing(self):
        print("Edit Car Details")

    def ViewUserProfile(self, UserID):
        print("View User Profile")


class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    Rating = models.IntegerField()
    Comment = models.CharField(max_length=255)
    Reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    CarSold = models.ForeignKey(Car, on_delete=models.CASCADE)

    def AddReview(self):
        print("Add Review")

    def EditReview(self):
        print("Edit Review")

    def DeleteReview(self):
        print("Delete Review")


class Message(models.Model):
    MessageID = models.AutoField(primary_key=True)
    Sender = models.CharField(max_length=255)
    Recipient = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    TimeStamp = models.DateTimeField(auto_now_add=True)

    def SendMessage(self):
        print("Send Message")

    def ReceiveMessage(self):
        print("Receive Message")

    def DeleteMessage(self):
        print("Delete Message")


class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    listing_name = models.CharField(max_length=255)
    listing_description = models.CharField(max_length=255)
    listing_price = models.IntegerField()
    listing_location = models.CharField(max_length=255)
    listing_image = models.CharField(max_length=255)
    subject = models.ForeignKey(Car, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing_id} {self.listing_name} {self.listing_description} {self.listing_price} {self.listing_location} {self.listing_image}"



