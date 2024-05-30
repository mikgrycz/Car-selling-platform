# Django imports
from django.urls import path
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Car, User, Message, Review, Transaction, SuperUser, Listing
from .serializers import CarSerializer, UserSerializer, MessageSerializer, ReviewSerializer, TransactionSerializer, SuperUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
load_dotenv()

def send_car_details(recipient_email):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP(os.getenv('SERVER_MAIL'), 587)
    smtp_server.starttls()
    smtp_server.login(os.getenv('SERVER_MAIL'),os.getenv('SERVER_PASSWORD'))

    # Create the message
    message = MIMEText(f'Car details:\n\n')
    message['Subject'] = 'Car Details'
    message['From'] = os.getenv('SERVER_MAIL')
    message['To'] = recipient_email

    # Send the message
    smtp_server.send_message(message)
    smtp_server.quit()


# Refactored Django views
@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_car(request, car_id):
    try:
        car = Car.objects.get(CarID=car_id)
    except Car.DoesNotExist:
        raise NotFound(detail="Car not found")
    serializer = CarSerializer(car)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    data = request.data
    try:
        user = User.objects.get(UserName=data['username'])
    except User.DoesNotExist:
        raise NotFound(detail="User not found")
    if user.UserPassword != data['password']:
        return Response("Incorrect password", status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

from os import makedirs
from os.path import join
from django.core.mail import send_mail

# Refactored Django views
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reviews(request, car_id):
    reviews = Review.objects.filter(CarSoldID=car_id)
    if not reviews:
        raise NotFound(detail="Reviews not found")
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_superusers(request):
    superusers = SuperUser.objects.all()
    serializer = SuperUserSerializer(superusers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ... Repeat the pattern for other POST endpoints ...

@api_view(['POST'])
def create_dir(request):
    dir = request.data.get('dir')
    if dir:
        dir_path = join('Public', 'CarData', dir)
        makedirs(dir_path, exist_ok=True)
        return Response({'message': 'Directory created'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'Directory name is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def buy_item(request, id):
    # Assuming 'send_car_details' is a function that sends an email with car details
    send_car_details("mikolajgrycz@gmail.com")
    return Response({"message": "Purchase successful and email sent"}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class MessageView(View):
    def post(self, request):
        data = json.loads(request.body)
        message = Message.objects.create(**data)
        return JsonResponse({'message': message.id})

class ReviewView(View):
    def post(self, request):
        data = json.loads(request.body)
        review = Review.objects.create(**data)
        return JsonResponse({'review': review.id})

class CarView(View):
    def post(self, request):
        data = json.loads(request.body)
        car = Car.objects.create(**data)
        return JsonResponse({'car': car.id})

class TransactionView(View):
    def post(self, request):
        data = json.loads(request.body)
        transaction = Transaction.objects.create(**data)
        return JsonResponse({'transaction': transaction.id})

class SuperUserView(View):
    def post(self, request):
        data = json.loads(request.body)
        superuser = SuperUser.objects.create(**data)
        return JsonResponse({'superuser': superuser.id})

class ListingView(View):
    def get(self, request, listing_id=None):
        if listing_id:
            listing = get_object_or_404(Listing, listing_id=listing_id)
            return JsonResponse(listing.__dict__)
        else:
            listings = list(Listing.objects.values())
            return JsonResponse({'listings': listings})

    def post(self, request):
        data = json.loads(request.body)
        listing = Listing.objects.create(**data)
        return JsonResponse({'listing': listing.id})