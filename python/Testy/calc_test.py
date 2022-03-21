import unittest
import Testy.calc as x


class calcTest(unittest.TestCase):

    def test_suma(self):
        wynik = x.suma(3, 6)
        self.assertEqual(wynik, 4)

    def test_roznica(self):
        wynik = x.roznica(4, 2)
        self.assertEqual(wynik, 2)


