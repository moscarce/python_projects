import unittest
from math import pi

from class_activity.question_4 import CircleArea


class test_area_of_circle(unittest.TestCase):
    def test_area(self):
        circle_area = CircleArea()
        self.assertAlmostEqual(circle_area.area_of_circle(1),pi)
        self.assertAlmostEqual(circle_area.area_of_circle(0),0)
        self.assertAlmostEqual(circle_area.area_of_circle(2),pi * 4)

    def test_value(self):
        circle_area = CircleArea()
        self.assertRaises(ValueError,circle_area.area_of_circle,-1)
        self.assertRaises(ValueError,circle_area.area_of_circle,-5)

    def test_radius_type(self):
        circle_area = CircleArea()
        self.assertRaises(TypeError, circle_area.area_of_circle, 2 + 5j)
        # self.assertRaises(TypeError, circle_area.area_of_circle, True)
