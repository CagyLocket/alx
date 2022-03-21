# Ćwiczenie 86
#
# Napisz program z wykorzystaniem pliku dat stanowiącym prostą bazę danych. ❑ Program składa się z 3 części:
# ❑ Moduł zarządzania firmami
# ❑ Dodaj firmę, Usuń firmę, Pokaż firmy
# ❑ Moduł pracownicy
# ❑ Dodaj pracownika, Usuń pracownika, Wyświetl pracowników
# ❑ Moduł zatrudnienie
# ❑ Przypisz firmę do pracownika, Usuń firmę pracownikowi, Zatrudnienie pracownika
# Uwaga! Jeden pracownik może być zatrudniony w wielu firmach
#
# * Usunięcie firmy nie powinno być możliwe jeżeli posiada pracowników
# ❑ * Usuniecie pracownika nie powinno być możliwe jeżeli posiada zatrudnienie.


class Pracownik:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def __str__(self):
        return f"Imię: {self.first_name}, Nazwisko: {self.last_name}"


class Firma:

    def __init__(self, name):
        self.__name = name
        self.__patients = []

    @property
    def name(self):
        return self.__name


    @property
    def patients(self):
        return self.__patients

    @name.setter
    def name(self, name):
        self.__name = name

    @patients.setter
    def patients(self, patients):
        self.__patients = patients

    def __str__(self):
        return f"Nazwa: {self.name}, Lista pacjentów: {self.patients}"


class FirmController:

    def __init__(self):
        self.__firms = []
        self.__employees = []

    @property
    def firms(self):
        return self.__firms

    @firms.setter
    def firms(self, firms):
        self.__firms = firms

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    def __str__(self):
        return f"{self.firms}, {self.employees}"

    def add_firm(self, name):
        """ Adds a firm"""

        firm = Firma(name)
        self.firms.append(firm)
        print(f"Firma {firm.name} została pomyślnie dodana.")

    def remove_firm(self, firm_name):
        """Removes a firm"""

        is_found = False
        for i in self.firms:
            if firm_name == i.name:
                is_found = True
                is_remove = input(f"Czy na pewno chcesz usunąć firmę'{i.name}' ? T/N ").upper()
                if is_remove == "T":
                    self.firms.remove(i)
                    print(f"Firma: {i.name} została pomyślnie usunięta.")
                    break
        if not is_found:
            print("Nie znaleziono firmy.")

    def add_employee(self, first_name, last_name):
        """ Adds an employee"""

        employee = Pracownik(first_name, last_name)
        self.employees.append(employee)
        print(f"Pracownik {employee.first_name} {employee.last_name} został pomyślnie dodana.")

    def remove_employee(self, last_name):
        """Removes an employee"""

        is_found = False
        for i in self.firms:
            if firm_name == i.name:
                is_found = True
                is_remove = input(f"Czy na pewno chcesz usunąć firmę'{i.name}' ? T/N ").upper()
                if is_remove == "T":
                    self.firms.remove(i)
                    print(f"Firma: {i.name} została pomyślnie usunięta.")
                    break
        if not is_found:
            print("Nie znaleziono firmy.")


















    def add_patient_to_clinic(self, clinic_name):
        """Adds a patient to a clinic"""

        is_found = False
        for i in self.clinics:
            if clinic_name == i.name:
                is_found = True

                first_name = input("Imię: ")
                last_name = input("Nazwisko: ")
                patient = Pacjent(first_name, last_name)
                i.patients.append(patient)
                print(f"Pacjent: {patient.first_name} {patient.last_name} został pomyślnie dodany do przychodni {clinic_name}")

        if not is_found:
            print("Nie znalzeiono przychodni.")

    def remove_patient_from_clinic(self, clinic_name):
        """Removes a patient from a cclinic"""

        is_found = False
        for i in self.clinics:
            if clinic_name == i.name:
                is_found = True
                last_name = input("Podaj nazwisko pacjenta: ")
                for j in i.patients:
                    if last_name == j.last_name:
                        is_remove = input(f"Czy na pewno chcesz usunąć pacjenta"
                                          f" '{j.first_name} {j.last_name}' ? T/N ").upper()
                        if is_remove == "T":
                            i.patients.remove(j)
                            print(f"Pacjent: {j.first_name} {j.last_name} został pomyślnie usunięty"
                                  f" z kliniki {clinic_name}.")
                            break
                        else:
                            break
        if not is_found:
            print("Nie znaleziono przychodni.")

    def list_firms(self):
        """Lists firms"""

        print("Lista firm:")
        my_sum = 0
        for i in self.firms:
            my_sum += 1
            print(f"{my_sum}. Nazwa: {i.name}")

    def list_patients(self, clinic_name):
        """Lists patients"""

        is_found = False
        for i in self.clinics:
            if clinic_name == i.name:
                is_found = True
                print(f"Lista pacjentów w przychodni {clinic_name}:")
                counter = 0
                for k in i.patients:
                    counter += 1
                    print(f"{counter}. {k.first_name} {k.last_name} ")

        if not is_found:
            print("Nie znaleziono przychodni.")

    def add_disease(self, last_name):
        is_found = False
        for i in self.clinics:
            for j in i.patients:
                if last_name == j.last_name:
                    is_found = True
                    disease = input("Dodaj chorobę: ")
                    j.diseases.append(disease)
                else:
                    break
        if not is_found:
            print("Nie znaleziono pacjenta.")

    def list_diseases(self, last_name):
        is_found = False
        for i in self.clinics:
            for j in i.patients:
                if last_name == j.last_name:
                    is_found = True
                    print(f"Pacjent: {j.first_name} {j.last_name}, Choroby: ", end="")
                    for k in j.diseases:
                        print(f"{k}, ", end="")
                    print()
                else:
                    break
        if not is_found:
            print("Nie znaleziono pacjenta.")


class FirmSystem(FirmController):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while True:

            menu = input(f"1-Firma, 2-Pracownicy, 3- Zatrudnienie 4-Koniec:").upper()
            if menu == "1":

                while True:

                    menu = input(f"1-Dodaj firmę, 2-usuń firmę, 3-Pokaż firmy, 4-wyjdź:").upper()

                    # 1-Dodaj firmę
                    if menu == "1":
                        name = input("Podaj nazwę firmy: ")
                        self.add_firm(name)

                    # 2-usuń firmę
                    elif menu == "2":
                        if self.firms:
                            firm_name = input("Podaj nazwę firmy: ")
                            self.remove_firm(firm_name)
                        else:
                            print("Nie znaleziono firmy.")

                    # 5-Pokaż firmy
                    elif menu == "3":
                        if self.firms:
                            self.list_firms()
                        else:
                            print("Brak firm.")

                    # 4-wyjdź
                    elif menu == "4":
                        break

                    else:
                        print("Nierozpoznana opcja menu")

            elif menu == "2":

                while True:

                    menu = input(f"1-Dodaj pracownika, 2-Usuń pracownika, 3-Wyświetl pracowników, 4-wyjdź,"
                                 ).upper()

                    # 1-Dodaj pracownika
                    if menu == "1":
                        first_name = input("Podaj imię: ")
                        last_name = input("Podaj nazwisko: ")
                        self.add_employee(first_name, last_name)

                    # 2-Usuń pracownika
                    elif menu == "2":
                        last_name = input("Podaj nazwisko pracownika: ")
                        self.remove_employee(last_name)

                    # 3-Wyświetl pracowników
                    elif menu == "3":
                        last_name = input("Podaj nazwisko pracownika: ")
                        pass

                    # 3-wyjdź
                    elif menu == "4":
                        break
                    else:
                        print("Nierozpoznana opcja menu")

            elif menu == "3":
                print("System zamknięto poprawnie.")
                break
            else:
                print("Nierozpoznana opcja menu")


nfz = FirmSystem()
