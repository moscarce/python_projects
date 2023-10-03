class NoNegativeHours(Exception):
    def __init__(self):
        super().__init__("Cannot work for 0 or less hours")


class Employee:
    __hourly_rate = 10
    __emp_id = 0

    def __init__(self, emp_name:str):
        self.__emp_id += 1
        self.__emp_name = emp_name
        self.__emp_department = None
        self.__emp_salary = 0
        self.__number_of_hours_worked = 0
        self.__salary = 0

    def calculate_emp_salary(self, number_of_hours_worked):
        if number_of_hours_worked > 0:
            self.__number_of_hours_worked = number_of_hours_worked
            self.__salary = self.__hourly_rate * number_of_hours_worked
            return self.__salary
        else:
            raise NoNegativeHours

    def emp_assign_department(self,department:str):
        self.__emp_department = department

    def print_employee_details(self):
        print(f'''
*************************************************************
Employee ID : {self.__emp_id}
Employee Name : {self.__emp_name}
Employee Department : {self.__emp_department}
Employer Hourly Rate : ${self.__hourly_rate}
Employer Number of Hours Worked : {self.__number_of_hours_worked}
Employee Salary : ${self.__salary}
*************************************************************
        ''')




