from tkinter import FIRST
from django.urls import path
from . import views
from .views import Index, FirstAnswer

urlpatterns = [
    path('', Index.as_view(), name='landing'),
    path('1/', FirstAnswer.as_view(), name='FAR')
]