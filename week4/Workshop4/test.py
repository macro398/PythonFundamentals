import unittest
from workshop4 import User, BankUser


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.user = User('Bob', 1234, 'password')
        #self.bank_user = BankUser('Bob', 1234, 'password')
        #self.bank_user1 = BankUser('Alice', 4242, 'allie123')

    @unittest.skip("demonstrating skipping")
    def test_user_name(self):
        self.assertEqual(self.user.name, 'Bob')

    def test_pin(self):
        self.assertEqual(self.user.pin, 1234)

    def test_change_name(self):
        self.user.change_name("Robert")
        self.assertEqual(self.user.name, "Robert")

    def test_change_pin(self):
        self.user.change_pin(4321)
        self.assertEqual(self.user.pin, 4321)

    def test_change_password(self):
        self.user.change_password("newpassword")
        self.assertEqual(self.user.password, "newpassword")

    #def test_bank_user_name(self):
        self.assertEqual(self.bank_user.name, 'Bob')

    #def test_bank_user_class(self):
         self.assertIsInstance(self.bank_user, User)

    # def test_bu_balance(self):
    #     new_bank_user = BankUser('Broke Bob', 1234, 'password')
    #     self.assertTrue(new_bank_user.balance == 0)

    # def test_show_balance(self):
    #     self.assertEqual(self.bank_user.show_balance(), None)

    # def test_withdraw(self):
    #     new_bank_user = BankUser('Broke Bob', 1234, 'password')
    #     new_bank_user.withdraw(100)
    #     self.assertTrue(new_bank_user.balance == -100)

    # def test_deposit(self):
    #     new_bank_user = BankUser('Broke Bob', 1234, 'password')
    #     new_bank_user.deposit(100)
    #     self.assertTrue(new_bank_user.balance == 100)