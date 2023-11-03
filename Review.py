from Client import Client
from Car import Car
class Review:
    ReviewID = 0
    Rating = 0
    Comment = ""
    Reviewer = Client()
    CarSold = Car()
    def AddReview(self):
        print("Add Review")
    def EditReview(self):
        print("Edit Review")
    def DeleteReview(self):
        print("Delete Review")