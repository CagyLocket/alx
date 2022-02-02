# Ex. J25-3

# ❑ Zaprojektuj program dzienniczek, który będzie umożliwiał:

# ❑ Dodawanie uczniów, wstawianie ocen uczniom, prezentowanie uczniów
# wraz z ocenami i średnią, usuwanie uczniów, modyfikacja uczniów (imie,nazwisko)

# ❑ Utwórz klasę uczeń, która:

# ❑ Będzie zawierała pola prywatne: imie, nazwisko i oceny
# ❑ Będzie zawierała konstruktor, który ustawi odpowiednie wartości dla pól imię, nazwisko
# ❑ Będzie zawierała metodę dodajOcene(iocena)
# ❑ Będzie zawierała metodę wyswietlOceny()
# ❑ Będzie zawierała metodę zwracającą sredniaOcen()
# ❑ Będzie zawierała gettery i setery (imię, nazwisko)
# ❑ Będzie zawierała metodę __str__()

# ❑ Utwórz menu: D-dodaj ucznia, P-pokaz uczniów, O – dodaj ocenę, U – usuń ucznia, M –modyfikuj, K - koniec


class Student:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grades = []

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def grades(self):
        return self.__grades

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @grades.setter
    def grades(self, grades):
        self.__grades = grades

    def __str__(self,):
        return f"Imię: {self.first_name} Nazwisko: {self.last_name} Oceny: {self.grades}"


class StudentController:

    def __init__(self):
        self.student_list = []

    def add_student(self, first_name, last_name):
        """Adds a student"""

        student = Student(first_name, last_name)
        self.student_list.append(student)
        print(f"Student {student.first_name} {student.last_name} został pomyślnie dodany.")

    def show_student(self):
        """Lists students"""

        if self.student_list:
            print("Lista studentów: ")
            for i in self.student_list:
                print(f"Imię: {i.first_name} Nazwisko: {i.last_name} Średnia ocen: {self.find_mean()} Oceny: {i.grades}")
        else:
            print("Brak studentów w dzienniku")

    def remove_student(self, last_name):
        """Removes a student"""

        is_found = False
        for i in self.student_list:
            if last_name == i.last_name:
                is_found = True
                is_remove = input(f"Czy na pewno chcesz usunąć studenta '{i.first_name} {i.last_name}' ? T/N ").upper()
                if is_remove == "T":
                    self.student_list.remove(i)
                    print(f"Student: {i.first_name} {i.last_name} został pomyślnie usunięty.")
                    break
                else:
                    break
        if not is_found:
            print("Nie znaleziono studenta o podanym nazwisku.")

    def modify_student(self, last_name):
        """Modifies student's properties"""

        is_found = False
        for i in self.student_list:
            if last_name == i.last_name:
                is_found = True
                while True:

                    menu2 = input("Wybierz opcję:\n1-zmień imię, 2-zmień nazwisko, 3-wyświetl studenta, 4-koniec").upper()

                    if menu2 == "1":
                        new_first_name = input(f"Aktualne imię: {i.first_name} >>> Podaj nowe imię: ")
                        i.first_name = new_first_name
                    elif menu2 == "2":
                        new_last_name = input(f"Aktualne nazwisko: {i.last_name} >>> Podaj nowe nazwisko: ")
                        i.last_name = new_last_name
                    elif menu2 == "3":
                        print(f"Imię: {i.first_name} Nazwisko: {i.last_name}")
                    elif menu2 == "4":
                        break
                    else:
                        print("Nierozpoznana opcja menu")

                print(f"Dane studenta: {i.first_name} {i.last_name} zostały pomyślnie zmienione.")
        if not is_found:
            print("Nie znaleziono studenta o podanym nazwisku.")

    def is_student(self, d):
        """Boolean to check is_student"""

        for i in self.student_list:
            if d == i.last_name:
                return True
            else:
                return False

    def add_grade(self, last_name):
        """Ads a grade for a student"""
        is_found = False
        for i in self.student_list:
            if last_name == i.last_name:
                is_found = True
                grade = int(input("Podaj ocenę: "))
                i.grades.append(grade)
                print(f"Pomyślnie dodano ocenę: {grade}")

        if not is_found:
            print("Nie znaleziono studenta o podanym nazwisku.")

    def show_grades(self, last_name):
        """Lists grades of a student"""

        is_found = False
        for i in self.student_list:
            if last_name == i.last_name:
                is_found = True
                print(f"Student: {i.first_name} {i.last_name} Oceny: {i.grades}")
        if not is_found:
            print("Nie znaleziono studenta o podanym nazwisku.")

    def find_mean(self):
        """Calculates a mean value for student's grades"""

        my_sum = 0
        for i in self.student_list:
            if len(i.grades) != 0:
                for j in i.grades:
                    my_sum += j
                mean = round(my_sum / len(i.grades), 2)
                return mean
            else:
                return "-"

    def __str__(self):
        return f"{self.student_list}"


class SchoolSystem(StudentController):

    def __init__(self, school_name):
        super().__init__()
        self.school_name = school_name
        self.menu()

    def menu(self):

        while True:

            menu = input(f"Witaj w szkole: {self.school_name}\nD-dodaj ucznia, P-pokaz uczniów, O – dodaj ocenę,"
                         " W-wyświetl oceny, U – usuń ucznia, M –modyfikuj, K - koniec").upper()

            if menu == "D":
                first_name = input("Podaj imię: ")
                last_name = input("Podaj nazwisko: ")
                self.add_student(first_name, last_name)

            elif menu == "P":
                # prezentacja: Imie:... Nawisko:...
                self.show_student()

            elif menu == "U":
                # pytania: nazwisko
                if self.student_list:
                    last_name = input("Podaj nazwisko studenta: ")
                    self.remove_student(last_name)
                else:
                    print('Brak studentów w dzienniku.')

            elif menu == "O":
                # pytania: nazwisko, ocena
                if self.student_list:
                    last_name = input("Podaj nazwisko studenta: ")
                    self.add_grade(last_name)
                else:
                    print("Nie znaleziono studenta o podanym nazwisku (2).")

            elif menu == "M":
                # pytania: nazwisko, noweImie, noweNazwisko, nowa_ocena
                if self.student_list:
                    last_name = input("Podaj nazwisko studenta: ")
                    self.modify_student(last_name)
                else:
                    print("Brak studentów w dzienniku.")

            elif menu == "W":
                # pytania: nazwisko
                if self.student_list:
                    last_name = input("Podaj nazwisko studenta: ")
                    self.show_grades(last_name)
                else:
                    print("Brak studentów w dzienniku.")

            elif menu == "K":
                break
            else:
                print("Nierozpoznana opcja menu")


school = SchoolSystem("Python is Fun")
