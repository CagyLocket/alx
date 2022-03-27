def main():

    """ wzorzec programowania: tak działa dekorator"""

    def dodaj_wydruki(f):
        def wrapper(*args, **kwargs):
            print("Start funkcji")
            result = f(*args, **kwargs)
            print("Koniec funkcji")
            return result
        return wrapper

    def kwadrat(x):
        print("Liczę kwadrat z", x)
        return x ** 2

    kwadrat_z_wydrukami = dodaj_wydruki(kwadrat)
    rezultat = kwadrat_z_wydrukami(2)
    assert rezultat == 4


    @dodaj_wydruki
    def szescian(x):
        print("Liczę kwadrat z", x)
        return x ** 3
    # @dodaj_wydruki przed definiacją funkcji znaczy to samo co po definicji zrobienie"
    # szescian = dodaj_wydruki(szescian)
    print(szescian(4))


if __name__ == '__main__':
    main()
