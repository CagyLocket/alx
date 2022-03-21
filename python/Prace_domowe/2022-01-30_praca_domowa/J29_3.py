# ❑ Zaprojektuj system dla firmy szkoleniowej, tak by było można utworzyć kurs,
# przypisać do niego trenera/trenerów oraz kursantów.
# ❑ Klasa Kursant, będzie posiadała pola prywatne: imie, nazwisko, email
# ❑ Klasa Trener, będzie posiadała pola prywatne : imie, nazwisko, specjalizacja
# ❑ Klasa Kurs, która będzie posiadała pola prywatne: nazwa kursu, trener (np.: dwóch trenerów
# może prowadzić jeden kurs), termin, uczestnicy (może być wielu), miejsce (miasto)
#
# ❑ Utwórz menu z opcjami: Dodaj kurs, Dodaj trenera do kursu, Dodaj uczestnika do kursu, Usuń
# trenera z kursu, Usuń uczestnika z kursu, Usuń kurs, Zmodyfikuj dane uczestnika, Zmodyfikuj dane
# kursu, Wyświetl kursy wraz z trenerami prowadzącymi oraz uczestnikami.
#
# ❑ Zadbaj o to, że kursu nie można usunąć jeżeli są przypisani do niego już uczestnicy.
# ❑ Maksymalna liczba uczestników na kursie to 5 osób.

class Personal:
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @email.setter
    def email(self, email):
        self.__email = email


class Kursant(Personal):

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"


class Trener(Personal):

    def __init__(self, first_name, last_name, email, specialization):
        super().__init__(first_name, last_name, email)
        self.__specialization = specialization

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        self.__specialization = specialization

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.specialization}"


class Kurs:

    def __init__(self, name, location, timestamp):
        self.__name = name
        self.__location = location
        self.__timestamp = timestamp
        self.__lecturers = []
        self.__learners = []

    @property
    def name(self):
        return self.__name

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def location(self):
        return self.__location

    @property
    def lecturers(self):
        return self.__lecturers

    @property
    def learners(self):
        return self.__learners

    @name.setter
    def name(self, name):
        self.__name = name

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

    @location.setter
    def location(self, location):
        self.__location = location

    @lecturers.setter
    def lecturers(self, lecturers):
        self.__lecturers = lecturers

    @learners.setter
    def learners(self, learners):
        self.__learners = learners

    def __str__(self):
        return f"Nazwa: {self.name}, Miejsce: {self.location}, Data: {self.timestamp}, Trenerzy: {self.lecturers}, " \
               f"Kursanci: {self.learners}"


class CourseController:

    def __init__(self):
        self.__course_list = []

    @property
    def course_list(self):
        return self.__course_list

    @course_list.setter
    def course_list(self, course_list):
        self.__course_list = course_list

    def __str__(self):
        return f"{self.course_list}"

    def add_course(self, name, location, timestamp):
        """ Adds a course"""

        course = Kurs(name, location, timestamp)
        self.course_list.append(course)
        print(f"Kurs: {course.name} został pomyślnie dodany.")

    def remove_course(self, course_name):
        """Removes a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True
                if i.learners:
                    print("Nie można usunąć kursu, do którego przypisani są uczestnicy.")
                    break
                else:
                    is_remove = input(f"Czy na pewno chcesz usunąć kurs"
                                      f" '{i.name}' ? T/N ").upper()
                    if is_remove == "T":
                        self.course_list.remove(i)
                        print(f"Kurs: {i.name} został pomyślnie usunięty.")
                        break
                    else:
                        break
        if not is_found:
            print("Nie ma takiego kursu.")

    def add_lecturer_to_course(self, course_name):
        """Adds a lecturer to a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True

                first_name = input("Imię: ")
                last_name = input("Nazwisko: ")
                email = input("Email: ")
                specialization = input("Specjalizacja: ")
                lecturer = Trener(first_name, last_name, email, specialization)
                i.lecturers.append(lecturer)
                print(f"Trener: {lecturer.first_name} {lecturer.last_name} został pomyślnie dodany"
                      f" do kursu {course_name}.")

        if not is_found:
            print("Nie ma takiego kursu.")

    def remove_lecturer_from_course(self, course_name):
        """Removes a lecturer from a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True
                last_name = input("Podaj nazwisko trenera: ")
                for j in i.lecturers:
                    if last_name == j.last_name:
                        is_remove = input(f"Czy na pewno chcesz usunąć trenera"
                                          f" '{j.first_name} {j.last_name}' ? T/N ").upper()
                        if is_remove == "T":
                            i.lecturers.remove(j)
                            print(f"Trener: {j.first_name} {j.last_name} został pomyślnie usunięty.")
                            break
                        else:
                            break
        if not is_found:
            print("Nie ma takiego kursu.")

    def add_learner_to_course(self, course_name):
        """Adds a learner to a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True
                # print(len(i.learners))

                if len(i.learners) < 5:
                    first_name = input("Imię: ")
                    last_name = input("Nazwisko: ")
                    email = input("Email: ")
                    learner = Kursant(first_name, last_name, email)
                    i.learners.append(learner)
                    print(f"Kursant: {learner.first_name} {learner.last_name} został "
                          f"pomyślnie dodany do kursu {course_name}.")
                else:
                    print("Do kursu dodano już maksymalną liczbę 5 uczestników.")
                    break

        if not is_found:
            print("Nie ma takiego kursu.")

    def remove_learner_from_course(self, course_name):
        """Removes a learner from a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True
                last_name = input("Podaj nazwisko kursanta: ")
                for j in i.learners:
                    if last_name == j.last_name:
                        is_remove = input(f"Czy na pewno chcesz usunąć kursanta"
                                          f" '{j.first_name} {j.last_name}' ? T/N ").upper()
                        if is_remove == "T":
                            i.learners.remove(j)
                            print(f"Kursant: {j.first_name} {j.last_name} został pomyślnie usunięty.")
                            break
                        else:
                            break
        if not is_found:
            print("Nie ma takiego kursu.")

    def modify_learner(self, course_name):
        """Modifies attributes of a learner"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True
                is_student = False
                last_name = input("Podaj nazwisko kursanta: ")
                for j in i.learners:
                    if last_name == j.last_name:
                        is_student = True

                        while True:

                            menu2 = input(
                                "Wybierz opcję:\n1-zmień imię 2-zmień nazwisko 3-zmień email "
                                "4-wyświetl uczestnika 5-koniec").upper()

                            if menu2 == "1":
                                new_first_name = input(f"Aktualne imię: {j.first_name} >>> Podaj nowe imię: ")
                                j.first_name = new_first_name
                            elif menu2 == "2":
                                new_last_name = input(f"Aktualne nazwisko: {j.last_name} >>> Podaj nowe nazwisko: ")
                                j.last_name = new_last_name
                            elif menu2 == "3":
                                new_email = input(f"Aktualny email: {j.email} >>> Podaj nowy email: ")
                                j.email = new_email
                            elif menu2 == "4":
                                print(f"Imię: {j.first_name} Nazwisko: {j.last_name} Email: {j.email}")
                            elif menu2 == "5":
                                break
                            else:
                                print("Nierozpoznana opcja menu")

                        print(f"Dane kursanta: {j.first_name} {j.last_name} zostały pomyślnie zmienione.")
                if not is_student:
                    print("Nie ma takiego kursanta.")

        if not is_found:
            print("Nie ma takiego kursu.")

    def modify_course(self, course_name):
        """Modifies attributes of a course"""

        is_found = False
        for i in self.course_list:
            if course_name == i.name:
                is_found = True

                while True:
                    menu3 = input(f"Wybierz opcję:\n1-zmień nazwę 2-zmień datę 3-zmień miejscowość "
                                    f"4-wyświetl kurs, 5-koniec").upper()

                    if menu3 == "1":
                        new_name = input(f"Aktualna nazwa: {i.name} >>> Podaj nową nazwę: ")
                        i.name = new_name
                    elif menu3 == "2":
                        new_timestamp = input(f"Aktualna data: {i.timestamp} >>> Podaj nową datę: ")
                        i.timestamp = new_timestamp
                    elif menu3 == "3":
                        new_location = input(f"Aktualna miejscowość: {i.location} >>> Podaj nową miejscowość: ")
                        i.location = new_location
                    elif menu3 == "4":
                        print(f"Nazwa: {i.name} Miejscowość: {i.location} Data: {i.timestamp}")
                    elif menu3 == "5":
                        break
                    else:
                        print("Nierozpoznana opcja menu")

                print(f"Dane kursu: {i.name} zostały pomyślnie zmienione.")

        if not is_found:
            print("Nie znaleziono kursu.")

    def show_courses(self):
        """Lists courses"""

        print("Lista kursów:")
        my_sum = 0
        for i in self.course_list:
            my_sum += 1
            print(f"Kurs {my_sum}. Nazwa: {i.name}, Miejsce: {i.location}, Data: {i.timestamp}, ", end="")
            print("Trenerzy: ", end="")
            for j in i.lecturers:
                print(f"{j.first_name} {j.last_name}, ", end="")
            print(" Kursanci: ", end="")
            for k in i.learners:
                print(f"{k.first_name} {k.last_name}, ", end="")
            print()


class SchoolSystem(CourseController):

    def __init__(self, school_name):
        super().__init__()
        self.school_name = school_name
        self.menu()

    def menu(self):

        while True:

            menu = input(f"Witaj w szkole: {self.school_name}\n1-dodaj kurs, 2-dodaj trenera do kursu,"
                         f" 3-dodaj uczestnika do kursu, 4-usuń trenera z kursu,\n5-usuń uczestnika z kursu, "
                         f"6-usuń kurs, 7-zmodifikuj dane uczestnika, 8-zmodyfikuj dane kursu, 9-wyświetl kursy: "
                         ).upper()

            if menu == "1":
                name = input("Podaj nazwę kursu: ")
                location = input("Podaj miasto: ")
                timestamp = input("Podaj termin: ")
                self.add_course(name, location, timestamp)

            elif menu == "2":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.add_lecturer_to_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 3-dodaj uczestnika do kursu
            elif menu == "3":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.add_learner_to_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            #4 - usuń trenera z kursu
            elif menu == "4":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.remove_lecturer_from_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 5-usuń uczestnika z kursu
            elif menu == "5":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.remove_learner_from_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 6-usuń kurs
            elif menu == "6":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.remove_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 7-zmodifikuj dane uczestnika
            elif menu == "7":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.modify_learner(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 8-zmodifikuj dane kursu
            elif menu == "8":
                if self.course_list:
                    course_name = input("Podaj nazwę kursu: ")
                    self.modify_course(course_name)
                else:
                    print("Nie znaleziono kursu.")

            # 7-wyświetl kursy
            elif menu == "9":
                if self.course_list:
                    self.show_courses()
                else:
                    print("Brak kursów.")

            elif menu == "K":
                break
            else:
                print("Nierozpoznana opcja menu")


school = SchoolSystem("Python is Fun")
