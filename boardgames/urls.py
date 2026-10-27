from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.list_games, name='list_games'),
]