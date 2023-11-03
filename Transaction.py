from Client import Client
from Car import Car
class Transaction:
    # interface for real transaction
    #test
    def InitiateTransaction(self) -> None:
        pass
    def CompleteTransaction(self):
        pass
    def CancelTransaction(self):
        pass

class RealTransaction(Transaction):   #### PROXY #####
    TransactionID = 0
    buyer = Client()
    seller = Client()
    car = Car()
    date = ""
    status = ""
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def InitiateTransaction(self):
        print("Initiate Transaction")
    def CompleteTransaction(self):
        print("Complete Transaction")
    def CancelTransaction(self):
        print("Cancel Transaction")

class ProxyTransaction(Transaction):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    def InitiateTransaction(self):
        self.realTransaction = RealTransaction(self.sender, self.receiver, self.amount)
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

