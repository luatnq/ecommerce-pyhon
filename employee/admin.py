from django.contrib import admin

from employee.models import Book, BookItem, Laptop, LaptopItem

# Register your models here.
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(Laptop)
admin.site.register(LaptopItem)