from django.contrib import admin
from .models import Car, User, Message, Review, Transaction, SuperUser, Listing
# Register your models here.

models = [Car, User, Message, Review, Transaction, SuperUser, Listing]
for model in models:
    admin.site.register(model)
 
