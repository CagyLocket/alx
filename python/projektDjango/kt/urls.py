from django.urls import path
from kt import views

urlpatterns = [
    path("", views.lista_kontaktow, name='lista_kontaktow'),
    path("dodaj_kontakt", views.dodaj_kontakt, name='dodaj_kontakt'),
    path("edytuj_kontakt/<int:pk>", views.edytuj_kontakt, name='edytuj_kontakt'),
    path("usun_kontakt/<int:pk>", views.usun_kontakt, name='usun_kontakt'),
]
