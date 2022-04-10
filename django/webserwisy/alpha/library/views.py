import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Book, Author
from .forms import AddBookForm, BookForm_ModelForm, DeleteBookForm


def home(request):
    browser = request.headers['USER-AGENT'].split()[-1]
    books = Book.objects.all()
    context = {
        'title': "Pierwsza strona",
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'browser': browser,
        'books': books,
    }

    # print(request.path, request.method, request.META, request.headers)
    return render(request, 'library/index.html', context)


def book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = DeleteBookForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["operation"] == 'delete':
                book.delete()
                messages.success(request, "Usunięto książkę")
                return HttpResponseRedirect(reverse("home"))
    delete_form = DeleteBookForm()
    context = {
        'book': book,
        'delete_form': delete_form,
    }
    return render(request, 'library/book.html', context)


def author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.book_set.all()
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'library/author.html', context)


def add_book(request):
    if request.method == "POST":
        # print(request.POST)
        form = AddBookForm(request.POST)
        if form.is_valid(): # srpawdza, czy wprowadzone dane są poprawne i uzupełnia pole cleaned_data w formularzu
            # print(form.cleaned_data)
            author = Author.objects.get(name=form.cleaned_data['author_name'])
            book = Book(
                title=form.cleaned_data['title'],
                author=author,
                description=form.cleaned_data['description']
            )
            book.save()
            # messages.add_message(request, messages.success, "Dodano książkę!")
            messages.success(request, "Dodano książkę!") # from django.contrib import messages
            return HttpResponseRedirect(book.get_absolute_url())

    else:
        form = AddBookForm()

    context = {
        'form': form,
    }

    return render(request, 'library/add_book.html', context)


def add_book_modelform(request):
    if request.method == "POST":
        form = BookForm_ModelForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Dodano książkę!")
            # return HttpResponseRedirect(reverse('book', args=(book.id,)))
            return HttpResponseRedirect(book.get_absolute_url())

    else:
        form = BookForm_ModelForm()

    context = {
        'form': form,
    }
    return render(request, 'library/add_book.html', context)
