from django import forms
from django.core.exceptions import ValidationError

from .models import Book, Author


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author_name = forms.CharField(max_length=200)
    # wybór obiketu? lepiej tak, o ile nie jest ich wiele
    # Tylko pamiętamy o zaimportowaniu modelu Author
    # author = forms.ModelChoiceField(Author.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 10}), required=False)

    #tworzymy własną walidację dla danego pola
    def clean_author_name(self):
        author_name = self.cleaned_data['author_name']
        if author_name != "Adam Mickiewicz":
            raise ValidationError("Obsługujemy tylko ksiązki Adama Mickiewicza")
        return author_name


class BookForm_ModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']


class DeleteBookForm(forms.Form):
    operation = forms.CharField(widget=forms.HiddenInput(), required=True, initial="delete")

