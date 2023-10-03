from unittest import TestCase

from pythonProject.oop.contact.contact import Contact


class TestContact(TestCase):
    def setUp(self) -> None:
        self.contact = Contact()

    def test_name_setters_and_getters(self):
        self.contact.set_name('tobi')
        self.assertEqual('tobi',self.contact.get_name())
