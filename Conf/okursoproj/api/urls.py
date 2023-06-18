from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('programacao/', programacao, name='list-courses-programmer'),
    path('design/', design, name='list-courses-design'),
]
