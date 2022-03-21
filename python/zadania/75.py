from tkinter import *

kontakty = []


class Kontakt:

    def __init__(self, imie, nazwisko, telefon, mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.mail = mail


def dodaj_kontakt():
    #pobieranie danych z formularza
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    telefon = entry_telefon.get()
    email = entry_email.get()

    kontakt = Kontakt(imie, nazwisko, telefon, email)
    kontakty.append(kontakt)

    # czyszczenie pól
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)

    #kursor wraca na to pole po kliknieciu dodaj kontakt
    entry_imie.focus()
    lista_kontaktow()

    print(kontakty)


def lista_kontaktow():

    listbox_lista_kontaktow.delete(0, END)
    for index, value in enumerate(kontakty):
        listbox_lista_kontaktow.insert(index, f"{value.imie} {value.nazwisko}")


def pokaz_szczegoly():
    #pobieramy index pola zaznaczonego w liscie kontaktów
    index = listbox_lista_kontaktow.index(ACTIVE)
    label_szczeg_imie_pusty.config(text=f"{kontakty[index].imie}")
    label_szczeg_nazwisko_pusty.config(text=f"{kontakty[index].nazwisko}")
    label_szczeg_telefon_pusty.config(text=f"{kontakty[index].telefon}")
    label_szczeg_email_pusty.config(text=f"{kontakty[index].mail}")


def usun_kontakt():
    index = listbox_lista_kontaktow.index(ACTIVE)
    kontakty.remove(kontakty[index]) # remove usuwa po wartości
    # kontakty.pop(index) # pop usuwa po indeksie
    lista_kontaktow()

def edytuj_kontakt():
    index = listbox_lista_kontaktow.index(ACTIVE)
    entry_imie.delete(0, END)
    entry_imie.insert(0, f"{kontakty[index].imie}") # wartość w insert mówi od którego znaku ma wstawiać
    entry_nazwisko.delete(0, END)
    entry_nazwisko.insert(0, f"{kontakty[index].nazwisko}")
    entry_telefon.delete(0, END)
    entry_telefon.insert(0, f"{kontakty[index].telefon}")
    entry_email.delete(0, END)
    entry_email.insert(0, f"{kontakty[index].mail}")

    label_nowy_kontakt.config(text="Edycja kontaktu:")
    button_dodaj_kontakt.config(text="Zmien kontakt", command=zmien_kontakt)


def zmien_kontakt():
    index = listbox_lista_kontaktow.index(ACTIVE)

    nowe_imie = entry_imie.get()
    nowe_nazwisko = entry_nazwisko.get()
    nowy_telefon = entry_telefon.get()
    nowy_email = entry_email.get()
    kontakty[index].imie = nowe_imie
    kontakty[index].nazwisko = nowe_nazwisko
    kontakty[index].telefon = nowy_telefon
    kontakty[index].email = nowy_email

    # czyszczenie pól
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_telefon.delete(0, END)
    entry_email.delete(0, END)

    label_nowy_kontakt.config(text="Nowy kontakt")
    button_dodaj_kontakt.config(text="Dodaj kontakt", command=dodaj_kontakt)
    lista_kontaktow()
    pokaz_szczegoly()


def test():








root = Tk()
root.title("Książka telefoniczna")
root.geometry("700x300")

ramka_lewa = Frame(root)
ramka_prawa = Frame(root)
ramka_dolna = Frame(root)

ramka_lewa.grid(row=0, column=0, pady=20, padx=20, sticky=N)
ramka_prawa.grid(row=0, column=1, pady=20, sticky=N)
ramka_dolna.grid(row=1, column=0, columnspan=2, sticky=W, padx=20)

label_lista_kontaktow = Label(ramka_lewa, text="Lista kontaktów")
listbox_lista_kontaktow = Listbox(ramka_lewa, width=30, height=7)
button_pokaz_szczegoly = Button(ramka_lewa, text="Pokaż szczegóły kontaktu", command=pokaz_szczegoly)
button_usun_kontakt = Button(ramka_lewa, text="Usuń kontakt", command=usun_kontakt)
button_edytuj_kontakt = Button(ramka_lewa, text="Edytuj kontakt", command=edytuj_kontakt)

label_lista_kontaktow.grid(row=0, column=0, columnspan=3)
listbox_lista_kontaktow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_usun_kontakt.grid(row=2, column=1)
button_edytuj_kontakt.grid(row=2, column=2)


#Ramka prawa
label_nowy_kontakt = Label(ramka_prawa, text="Nowy kontakt:")
label_imie = Label(ramka_prawa, text="Imię:")
label_nazwisko = Label(ramka_prawa, text="Nazwisko:")
label_telefon = Label(ramka_prawa, text="Telefon:")
label_email = Label(ramka_prawa, text="Email:")
# button_dodaj_kontakt = Button(ramka_prawa, text="Dodaj kontakt", command=dodaj_kontakt)
button_dodaj_kontakt = Button(ramka_prawa, text="Dodaj kontakt", command=lambda: test("*"))


entry_imie = Entry(ramka_prawa, background="#404040", foreground="#FFFFFF")
entry_nazwisko = Entry(ramka_prawa, width=30)
entry_telefon = Entry(ramka_prawa)
entry_email = Entry(ramka_prawa)

label_nowy_kontakt.grid(row=0, column=0, columnspan=2)
label_imie.grid(row=1, column=0, sticky=W)
label_nazwisko.grid(row=2, column=0, sticky=W)
label_telefon.grid(row=3, column=0, sticky=W)
label_email.grid(row=4, column=0, sticky=W)
button_dodaj_kontakt.grid(row=5, column=0, columnspan=2)
entry_imie.grid(row=1, column=1, sticky=W)
entry_nazwisko.grid(row=2, column=1, sticky=W)
entry_telefon.grid(row=3, column=1, sticky=W)
entry_email.grid(row=4, column=1, sticky=W)

# Ramka dolna
label_szczeg_kontaktu = Label(ramka_dolna, text="Szczegóły kontaktu")
label_szczeg_imie = Label(ramka_dolna, text="Imię:")
label_szczeg_imie_pusty = Label(ramka_dolna, text="...", width=10)
label_szczeg_nazwisko = Label(ramka_dolna, text="Nazwisko:")
label_szczeg_nazwisko_pusty = Label(ramka_dolna, text="...", width=10)
label_szczeg_telefon = Label(ramka_dolna, text="Telefon:")
label_szczeg_telefon_pusty = Label(ramka_dolna, text="...", width=10)
label_szczeg_email = Label(ramka_dolna, text="Email:")
label_szczeg_email_pusty = Label(ramka_dolna, text="...", width=10)

label_szczeg_kontaktu.grid(row=0, column=0, columnspan=8, sticky=W)
label_szczeg_imie.grid(row=1, column=0, sticky=W)
label_szczeg_imie_pusty.grid(row=1, column=1, sticky=W)
label_szczeg_nazwisko.grid(row=1, column=2, sticky=W)
label_szczeg_nazwisko_pusty.grid(row=1, column=3, sticky=W)
label_szczeg_telefon.grid(row=1, column=4, sticky=W)
label_szczeg_telefon_pusty.grid(row=1, column=5, sticky=W)
label_szczeg_email.grid(row=1, column=6, sticky=W)
label_szczeg_email_pusty.grid(row=1, column=7, sticky=W)








root.mainloop()
