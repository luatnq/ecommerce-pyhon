from django.db import models

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    # def __str__(self):
    #     return self.bookName, self.barcode
    class Meta:
        db_table = "books"


class MobilePhone(models.Model):
    name = models.CharField(max_length=20)
    display = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    chip = models.CharField(max_length=20)
    camera = models.CharField(max_length=10)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    class Meta:
        db_table = "mobile_phone"

class Clothes(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    class Meta:
        db_table = "clothes"

class Laptop(models.Model):
    name = models.CharField(max_length=20)
    display = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    chip = models.CharField(max_length=20)
    camera = models.CharField(max_length=10)
    GPU = models.CharField(max_length=20)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    class Meta:
        db_table = "laptop"
    def set_stt(self, x):
        self.stt = x

class Shose(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    class Meta:
        db_table = "shose"

class Electronic(models.Model):
    name = models.CharField(max_length=20)
    producer = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    quantity = models.IntegerField()
    stt = models.IntegerField()

    class Meta:
        db_table = "electronic"

class Account(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    class Meta:
        db_table = "accounts"

class Fullname(models.Model):
    firstName = models.CharField(max_length=256)
    midName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)

    class Meta:
        db_table = "fullnames"

class Address(models.Model):
    numberHouse = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    city = models.CharField(max_length=256)

    class Meta:
        db_table = "address"

class Employee(models.Model):
    email = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    dob = models.DateField(null=True)
    name = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = "employee"

class BookItem(models.Model):
    name = models.CharField(max_length=256)
    discount = models.CharField(max_length=256)
    price = models.IntegerField(null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    urlImage = models.CharField(max_length=500)

    class Meta:
        db_table = "book_items"

class LaptopItem(models.Model):
    name = models.CharField(max_length=256)
    discount = models.CharField(max_length=256)
    price = models.IntegerField(null=True)
    urlImage = models.CharField(max_length=500)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "laptop_items"


class ClothesItem(models.Model):
    name = models.CharField(max_length=256)
    discount = models.CharField(max_length=256)
    price = models.IntegerField(null=True)
    urlImage = models.CharField(max_length=500)
    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "clothes_items"

