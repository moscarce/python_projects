from pythonProject.largest_difference import FullName
from unittest import TestCase


class TestFullname(TestCase):
    def setUp(self) -> None:
        self.fname = FullName()


    def test_fullname(self):
        self.assertEqual('G. C. Martins', self.fname.get_fullname('grace chigoziem martins'))
        self.assertEqual('G. Maduekwe', self.fname.get_fullname('grace maduekwe'))

    def test_sum(self):
        self.assertEqual(17, self.fname.sum_alpha_numeric('A12BCK0dt59'))
        self.assertEqual(13, self.fname.sum_alpha_numeric('A1-2BCK0dt59'))
