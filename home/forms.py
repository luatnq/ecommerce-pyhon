from django import forms
from employee.models import Book

class BookForm(forms.ModelForm):
	publication_date = forms.DateTimeInput()
	class Meta:
		model = Book
		fields = ('bookName', 'author', 'barcode' )