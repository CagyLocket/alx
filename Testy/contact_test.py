import unittest
import Testy.contact as contact

class Contact(unittest.TestCase):

    contact_1 = contact.Contact("Adam", "Nowak")
    contact_2 = contact.Contact("Jan", "Kowalski")

    def test_email(self):
        self.assertEqual(self.contact_1.email(), "Adam_Nowak@firma.pl")
        self.assertEqual(self.contact_2.email(), "Jan_Kowalski@firma.pl")

    def test_przedstaw_sie(self):
        self.assertEqual(self.contact_1.przedstaw_sie(), "Adam Nowak")
        self.assertEqual(self.contact_2.przedstaw_sie(), "Jan Kowalski")