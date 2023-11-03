from Client import Client
from datetime import datetime
class Message:
    MessageID = 0
    Sender = Client()
    Receipient = Client()
    Content = ""
    TimeStamp = datetime.now()
    def SendMessage(self):
        print("Send Message")
    def ReceiveMessage(self):
        print("Receive Message")
    def DeleteMessage(self):
        print("Delete Message")