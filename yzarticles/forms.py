from django import forms
from .models import Book,Entry

class BookFrom(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['text']
		lables = {"text":''}

class EntryFrom(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ["text"]
		lables = {"text":""}
		widgets = {'text':forms.Textarea(attrs={'cols':80})}