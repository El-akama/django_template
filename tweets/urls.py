from django.urls import path
from .views import TweetListView, TweetCreateView


urlpatterns = [
    path('', TweetListView.as_view(), name='home'),
    path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
]