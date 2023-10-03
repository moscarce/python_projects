from unittest import TestCase

from pythonProject.class_activity_2.second_largest_number import SecondLargest


class TestSecondLargest(TestCase):
    def test_second_largest_number(self):
        self.second_largest = SecondLargest()
        self.assertEqual(2, self.second_largest.check_second_largest('dfa12321afd'))
        self.assertEqual(-1, self.second_largest.check_second_largest('abc1111'))
