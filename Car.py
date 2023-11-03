class Car:
    CarID = 0
    Make = ""
    Model = ""
    Year = 0
    Price = 0
    Mileage = 0
    Description = ""
    SellerID = 0
    def GetCarDetails():
        print("CarID: " + str(Car.CarID) + "\nMake: " + Car.Make + "\nModel: " + Car.Model + "\nYear: " + str(Car.Year) + "\nPrice: " + str(Car.Price) + "\nMileage: " + str(Car.Mileage) + "\nDescription: " + Car.Description + "\nSellerID: " + str(Car.SellerID) + "\n")
    def SetCarDetails(CarID, Make, Model, Year, Price, Mileage, Description, SellerID):
        Car.CarID = CarID
        Car.Make = Make
        Car.Model = Model
        Car.Year = Year
        Car.Price = Price
        Car.Mileage = Mileage
        Car.Description = Description
        Car.SellerID = SellerID
