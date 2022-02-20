from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.


def lista_kontaktow(request):
    dane = Contact.objects.all()
    context = {"dane": dane}
    return render(request, "kt/lista_kontaktow.html", context)


def dodaj_kontakt(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        return redirect("lista_kontaktow")
    else:
        form = ContactForm()
        context = {"form": form}
        return render(request, "kt/dodaj_kontakt.html", context)


def edytuj_kontakt(request, pk):
    dane = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=dane)
        form.save()
        return redirect("lista_kontaktow")
    else:
        form = ContactForm(instance=dane)
        context = {"form": form}
        return render(request, "kt/edytuj_kontakt.html", context)


def usun_kontakt(request, pk):
    Contact.objects.filter(pk=pk).delete()
    return redirect("lista_kontaktow")
