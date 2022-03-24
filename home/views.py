
from random import randint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from employee.models import Book, BookItem, Laptop
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.core import serializers

from home.forms import BookForm

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def create_book(request):
    if(request.POST):
        book_data = request.POST.dict()
        bookName = book_data.get("bookName")
        author = book_data.get("author")
        quantity = book_data.get("quantity")
        barcode = "B" + str(randint(100, 2000))
        book = Book(bookName=bookName, author=author,
                    barcode=barcode, quantity=quantity, stt = 1)
        book.save()

        books = Book.objects.all().order_by('-id')
        i = 1
        for book in books:
            book.stt = i
            i += 1
        print(bookName, author, quantity)
        book_data['book_list'] = render_to_string(
            'home/book_list.html', {'books': books})

        return JsonResponse(book_data)
    return JsonResponse({'message': 'error'})


def book_list(request):
    books = Book.objects.all()
    i = 1
    for book in books:
        book.stt = i
        i += 1
    context = {
        'books': books
    }
    return render(request, 'home/index.html', context)


@csrf_protect
def laptop_list(request):
    data = dict()
    laptops = Laptop.objects.all().order_by('-id')
    i = 1
    for laptop in laptops:
        laptop.set_stt(i)
        i += 1
    data['laptop_list'] = render_to_string(
        'home/laptop_list.html', {'laptops': laptops})
    return JsonResponse(data)


def create_laptop(request):

    if(request.POST):
        laptop_data = request.POST.dict()
        name = laptop_data.get("name")
        display = laptop_data.get("display")
        producer = laptop_data.get("producer")
        chip = laptop_data.get("chip")
        camera = laptop_data.get("camera")
        GPU = laptop_data.get("GPU")
        barcode = "LT" + str(randint(100, 2000))
        quantity = laptop_data.get("quantity")

        laptop = Laptop(name=name, display=display, producer=producer, chip=chip,
                        camera=camera, GPU=GPU, barcode=barcode, quantity=quantity, stt = 1)
        laptop.save()
        return laptop_list(request)
    return JsonResponse({'message': 'error'})


def book_detail(request):
    data = request.POST.dict()
    book_id = data.get("id")
    print(book_id)
    book = Book.objects.get(id=book_id)

    # data['book_detail'] = ren
    return JsonResponse(serializers.serialize('json', [book]), safe=False)


def update_book(request):

    data = request.POST.dict()
    book = Book.objects.get(id=data.get("id"))
    print(data.get("bookName"))
    book.bookName = data.get("bookName")

    book.save()
    books = Book.objects.all().order_by('-id')
    i = 1
    for book in books:
        book.stt = i
        i += 1
    data['book_list'] = render_to_string(
        'home/book_list.html', {'books': books})
  
    return JsonResponse(data)

def save_book_item(request):
    
    data = request.POST.dict()
    name = data.get("name")
    discount = data.get("discount")
    price = data.get("price")
    urlImage = data.get("urlImage")
    bookItem = BookItem(name = name, discount = discount,
            price = price, urlImage = urlImage)
    bookItem.save()
    
    return JsonResponse({'status' : 'success'})