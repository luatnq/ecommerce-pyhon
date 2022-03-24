from unicodedata import name
from . import views
from django.urls import path

app_name = 'client'
urlpatterns = [
    path('', views.index, name = "client"),
]