from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
while len(name) > 10 or len(name) < 1:
    if len(name) > 10:
        print("Max name length is 10 characters")
    elif len(name) < 1 :
        print("You must enter a name.")
    name = input("Enter name to register: ")

pin = input("Enter PIN: ")
while True:
    if len(pin) != 4:
        print("PIN must contain 4 numbers.")
    else:
        break
    pin = input("Enter PIN: ")
balance = 0
print(f"{name} has been registered iwth a starting balance of ${balance}")

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(name)
        break
    