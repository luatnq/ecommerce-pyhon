from unicodedata import name
from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', views.book_list, name = 'home'),
    path('create_book', views.create_book, name = 'create_book'),
    path('create_laptop', views.create_laptop, name = 'create_laptop'),
    path('laptops', views.laptop_list, name = 'laptops')
]