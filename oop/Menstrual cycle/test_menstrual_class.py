from unittest import TestCase
from menstrual_class import MenstrualCycleTracker
from menstrual_class import SeeADoctor


class TestMenstrualCycle(TestCase):
    def setUp(self) -> None:
        self.tracker = MenstrualCycleTracker()
        self.tracker.set_cycle_length(23)


    def test_set_cycle_length(self):
        self.assertEqual(23, self.tracker.get_cycle_length())
        self.assertRaises(SeeADoctor, self.tracker.set_cycle_length, 20)

    def test_get_ovulation_day(self):
        self.assertEqual(9,self.tracker.get_ovulation_day())

    def test_get_possible_ovulation_test(self):
        self.assertEqual('7 - 11',self.tracker.get_possible_ovulation_days())

    def test_get_ovulation_days_full_length(self):
        self.assertEqual('2 - 11', self.tracker.get_ovulation_days_full_length())

