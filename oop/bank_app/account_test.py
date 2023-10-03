import unittest

from pythonProject.oop.bank_app.account import Account
from pythonProject.oop.custom_exception.amount_less_than_zero import AmountLessThanZero
from pythonProject.oop.custom_exception.incorrect_pin import IncorrectPin
from pythonProject.oop.custom_exception.insufficient_fund import InsufficientFund


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account('1','tobi','1234')


    def test_deposit(self):
        self.account.deposit(5000)
        self.assertEqual(5000,self.account.get_balance('1234'))
        self.account.deposit(5000)
        self.assertEqual(10000,self.account.get_balance('1234'))
        self.assertRaises(AmountLessThanZero,self.account.deposit,-5000)

    def test_get_balance_with_wrong_pin(self):
        self.account.deposit(5000)
        self.assertEqual(5000, self.account.get_balance('1234'))
        self.assertEqual(0, self.account.get_balance('1234567'))

    def test_withdrawal(self):
        self.account.deposit(5000)
        self.account.withdraw(3000,'1234')
        self.assertEqual(2000, self.account.get_balance('1234'))

    def test_withdrawal_with_wrong_pin(self):
        self.account.deposit(5000)
        self.assertRaises(IncorrectPin, self.account.withdraw,3000,'12345')
    def test_withdraw_more_than_balance(self):
        self.account.deposit(5000)
        self.assertRaises(InsufficientFund, self.account.withdraw,6000,'1234')


