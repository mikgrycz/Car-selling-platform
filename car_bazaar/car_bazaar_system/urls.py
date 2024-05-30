from django.urls import path
from .views import (
    send_car_details,
    get_cars,
    get_car,
    login,
    get_users,
    get_messages,
    get_reviews,
    add_review,
    get_transactions,
    get_superusers,
    create_user,
    create_dir,
    buy_item,
    MessageView,
    ReviewView,
    CarView,
   # UserView,
    TransactionView,
    SuperUserView,
    ListingView,
)
from .models import Car, User, Message, Review, Transaction, SuperUser, Listing
urlpatterns = [
    #path('cars/', CarView.as_view()),
   # path('users/', UserView.as_view()),    
    path('cars/', get_cars),
    path('car/<str:car_id>/', get_car),
    path('api/login/', login),
    path('users/', get_users),
    path('messages/', get_messages),
  #  path('reviews', add_review, name='add_review'),
    path('reviews/', ReviewView.as_view(), name='reviews/'),
    path('reviews/<int:car_id>/', ReviewView.as_view(), name='reviews_with_id'),
    path('add-review/<int:car_id>/', ReviewView.as_view(), name='add_review'),
    path('transactions/', get_transactions),
    path('superusers/', get_superusers),
    path('users/', create_user, name='create_user'),
    path('create-dir/', create_dir, name='create_dir'),
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('messages/', MessageView.as_view()),
    path('transactions/', TransactionView.as_view()),
    path('superusers/', SuperUserView.as_view()),
    path('listings/', ListingView.as_view()),
    path('listings/<str:listing_id>/', ListingView.as_view()),
]

# # Django URLs
# urlpatterns = [

# ]