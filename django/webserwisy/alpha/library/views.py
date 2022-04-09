from django.shortcuts import render


def home(request):
    context = {'title': "Pierwsza strona"}
    return render(request, 'library/index.html', context)
