class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self, new_name):
        self.name = new_name
        print(f"Name was changed to {new_name}")
    def change_pin(self, new_pin):
        self.pin = new_pin
        print(f"Name was changed to {new_pin}")
    def change_password(self, new_password):
        self.password = new_password
        print(f"Name was changed to {new_password}")

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name,pin,password)
        self.balance = 0

    def show_balance(self):
        print(self.balance)
    def withdraw(self,money):
        self.balance -= money
    def deposit(self,money):
        self.balance += money
    
    def transfer_money(self, user, money):
        print("Authentication required")
        pin = int(input("Enter your PIN: "))
        if user.pin == pin:
            user.deposit(money)
            self.withdraw(money)
            return True
        else:
            print("Invalid PIN: Transaction Cancelled.")
            return False

    def request_money(self, user, money):
        print("Authentication required")
        pin = int(input(f"Enter {user.name}'s PIN: "))
        if user.pin == pin:
            password = input("Please input password: ")
            if user.password == password:
                print("Request authorized")
                user.withdraw(money)
                self.deposit(money)
                return True
        else:
            print("Invalid PIN: Transaction Cancelled.")
            return False

''' Driver code for task 3 '''
#bob = BankUser('Bob', 1234, 'password')
#print(bob.name,bob.pin,bob.password,bob.balance)

'''driver code for task 4'''
'''bob = BankUser('Bob', 1234, 'password')
bob.show_balance()
bob.deposit(500)
bob.show_balance()
bob.withdraw(300)
bob.show_balance()'''

'''driver code for task 5'''
bob = BankUser('Bob', 1234, 'password')
alice = BankUser('alice', 4321, 'hello')

alice.deposit(5000)
alice.show_balance()
bob.show_balance()
alice.transfer_money(bob, 500)
alice.show_balance()
bob.show_balance()
if bob.balance == 500:
    alice.request_money(bob,250)
alice.show_balance()
bob.show_balance()