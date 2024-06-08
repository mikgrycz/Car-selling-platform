from rest_framework import serializers
from .models import User, Car, Transaction, RealTransaction, ProxyTransaction, SuperUser, Review, Message, Listing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    Seller = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Car
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class RealTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTransaction
        fields = '__all__'

class ProxyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProxyTransaction
        fields = '__all__'

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperUser
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    Reviewer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    CarSold = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = Review
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'