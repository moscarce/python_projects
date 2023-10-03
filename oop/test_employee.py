from unittest import TestCase

from oop.employee import Employee, NoNegativeHours


class TestEmployee(TestCase):

    def setUp(self) -> None:
        self.employee = Employee('Tomide')
    def test_calculate_emp_salary(self):
        self.assertEqual(100,self.employee.calculate_emp_salary(10))

    def test_cannot_calculate_emp_salary_if_hour_is_zero_or_less(self):
        self.assertRaises(NoNegativeHours,self.employee.calculate_emp_salary,-10)
        self.assertRaises(NoNegativeHours,self.employee.calculate_emp_salary,0)
    def test_assign_dept_and_print_emp_details(self):
        self.employee.calculate_emp_salary(10)
        self.employee.emp_assign_department('front end developer')
        self.employee.print_employee_details()

