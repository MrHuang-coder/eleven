import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.first = 'huang'
        self.last = 'haitao'
        self.salary = 1000000
        self.my_employee = Employee(self.first, self.last, self.salary)

    def test_gave_default(self):
        self.add = 4000
        self.my_employee.give_raise(self.add)
        self.assertEqual(self.salary + self.add, self.my_employee.annual_salary)

    def test_give_cusom_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.salary + 5000, self.my_employee.annual_salary)
