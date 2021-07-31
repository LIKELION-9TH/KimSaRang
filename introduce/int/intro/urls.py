from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('music/', views.music, name="music"),
    path('place/', views.place, name="place"),
]