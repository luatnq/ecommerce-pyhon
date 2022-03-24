from unicodedata import name
from . import views
from django.urls import path

app_name = 'home'
urlpatterns = [
    path('', views.book_list, name='home'),
    path('create_book', views.create_book, name='create_book'),
    path('create_laptop', views.create_laptop, name='create_laptop'),
    path('laptops', views.laptop_list, name='laptops'),
    path('book_detail', views.book_detail, name='book_detail'),
    path('update_book', views.update_book, name= 'update_book'),
    path('create_book_item', views.save_book_item, name= 'create_book_item')
]
