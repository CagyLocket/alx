# ❑ Zaprojektuj system dla NFZ.
# ❑ System ma za zadanie zbierać dla każdej przychodni informacje o swoich
# pacjentach oraz ich chorobach.
# ❑ Przychodnia zawiera informacje takie jak:
# nazwa, miasto, lista pacjentów
# ❑ Pacjent zawiera takie informacje jak:
# imię, nazwisko, lista chorób
#
# ❑ Zaprojektuj menu:
# ❑ 1 – Przychodnia, 2 – Pacjent, 3 – Koniec
# ❑ W opcji – 1:
# 1 – dodaj przychodnię, 2 - usuń przychodnię, 3 - dodaj pacjenta do przychodni, 3 – usuń pacjenta z przychodni
# 4 - lista przychodni, 5 - lista pacjentów w przychodni
# ❑ W opcji – 2:
# 1 – dodaj chorobę pacjentowi, 2 - lista chorób pacjenta


class Pacjent:

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__diseases = []

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def diseases(self):
        return self.__diseases

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @diseases.setter
    def diseases(self, diseases):
        self.__diseases = diseases

    def __str__(self):
        return f"Imię: {self.first_name}, Nazwisko: {self.last_name}, Lista chorób: {self.diseases}"


class Przychodnia:

    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__patients = []

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def patients(self):
        return self.__patients

    @name.setter
    def name(self, name):
        self.__name = name

    @location.setter
    def location(self, location):
        self.__location = location

    @patients.setter
    def patients(self, patients):
        self.__patients = patients

    def __str__(self):
        return f"Nazwa: {self.name}, Miejsce: {self.location}, Lista pacjentów: {self.patients}"


class ClinicController:

    def __init__(self):
        self.__clinics = []

    @property
    def clinics(self):
        return self.__clinics

    @clinics.setter
    def clinics(self, clinics):
        self.__clinics = clinics

    def __str__(self):
        return f"{self.clinics}"

    def add_clinic(self, name, location):
        """ Adds a clinic"""

        clinic = Przychodnia(name, location)
        self.clinics.append(clinic)
        print(f"Przychodnia: {clinic.name} została pomyślnie dodana.")

    def remove_clinic(self, clinic_name):
        """Removes a clinic"""

        is_found = False
        for i in self.clinics:
            if clinic_name == i.name:
                is_found = True
                is_remove = input(f"Czy na pewno chcesz usunąć przychodnię'{i.name}' ? T/N ").upper()
                if is_remove == "T":
                    self.clinics.remove(i)
                    print(f"Przychodnia: {i.name} została pomyślnie usunięta.")
                    break
        if not is_found:
            print("Nie znaleziono przychodni.")

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

    def list_clinics(self):
        """Lists clinics"""

        print("Lista przychodni:")
        my_sum = 0
        for i in self.clinics:
            my_sum += 1
            print(f"Nr {my_sum}. Nazwa: {i.name}, Miejsce: {i.location}")

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


class ClinicSystem(ClinicController):

    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):

        while True:

            menu = input(f"1-Przychodnia, 2-Pacjent, 3-Koniec:").upper()
            if menu == "1":

                while True:

                    menu = input(f"1-Dodaj przychodnię, 2-usuń przychodnię, 3-dodaj pacjenta do przychodni, "
                                 f"4-usuń pacjenta z przychodni,\n5-lista przychodni, 6-lista pacjentów w przychodni"
                                 f" 7-wyjdź:").upper()

                    # 1-Dodaj przychodnię
                    if menu == "1":
                        name = input("Podaj nazwę przychodni: ")
                        location = input("Podaj miasto: ")
                        self.add_clinic(name, location)

                    # 2-usuń przychodnię
                    elif menu == "2":
                        if self.clinics:
                            clinic_name = input("Podaj nazwę przychodni: ")
                            self.remove_clinic(clinic_name)
                        else:
                            print("Nie znaleziono przychodni.")

                    # 3-dodaj pacjenta do przychodni
                    elif menu == "3":
                        if self.clinics:
                            clinic_name = input("Podaj nazwę przychodni: ")
                            self.add_patient_to_clinic(clinic_name)
                        else:
                            print("Nie znaleziono przychodni.")

                    # 4-usuń pacjenta z przychodni
                    elif menu == "4":
                        if self.clinics:
                            clinic_name = input("Podaj nazwę przychodni: ")
                            self.remove_patient_from_clinic(clinic_name)
                        else:
                            print("Nie znaleziono przychodni.")

                    # 5-lista przychodni
                    elif menu == "5":
                        if self.clinics:
                            self.list_clinics()
                        else:
                            print("Brak przychodni.")

                    # 6-lista pacjentów w przychodni
                    elif menu == "6":
                        if self.clinics:
                            clinic_name = input("Podaj nazwę przychodni: ")
                            self.list_patients(clinic_name)
                        else:
                            print("Brak przychodni.")

                    # 7-wyjdź
                    elif menu == "7":
                        break

                    else:
                        print("Nierozpoznana opcja menu")

            elif menu == "2":

                while True:

                    menu = input(f"1-Dodaj chorobę pacjentowi, 2-lista chorób pacjenta, 3-wyjdź,"
                                 ).upper()

                    # 1-Dodaj chorobę pacjentowi
                    if menu == "1":
                        last_name = input("Podaj nazwisko pacjenta: ")
                        self.add_disease(last_name)

                    # 2-lista chorób pacjenta
                    elif menu == "2":
                        last_name = input("Podaj nazwisko pacjenta: ")
                        self.list_diseases(last_name)

                    # 3-wyjdź
                    elif menu == "3":
                        break
                    else:
                        print("Nierozpoznana opcja menu")

            elif menu == "3":
                print("System zamknięto poprawnie.")
                break
            else:
                print("Nierozpoznana opcja menu")


nfz = ClinicSystem()

