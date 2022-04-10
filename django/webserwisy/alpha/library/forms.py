from django import forms
from django.core.exceptions import ValidationError


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author_name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 10}))

    #tworzymy własną walidację dla danego pola
    def clean_author_name(self):
        author_name = self.cleaned_data['author_name']
        if author_name != "Adam Mickiewicz":
            raise ValidationError("Obsługujemy tylko ksiązki Adama Mickiewicza")
        return author_name

