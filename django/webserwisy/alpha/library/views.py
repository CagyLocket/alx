from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    context = {'title': "Pierwsza strona", 'dump': request}
    return render(request, 'library/index.html', context)

    # print(request.path, request.method, request.META)
    # return HttpResponse("Witaj na mojej stronie zbudowanej za pomocą widoku")


