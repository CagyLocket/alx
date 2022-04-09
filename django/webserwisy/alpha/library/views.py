import datetime

from django.shortcuts import render
from .models import Book, Author


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
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'library/book.html', context)


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    books = author.book_set.all()
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'library/author.html', context)
