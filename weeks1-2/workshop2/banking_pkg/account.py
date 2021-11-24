def show_balance(balance):
    print(f"Current balance: ${balance}")

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(balance) + float(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return float(balance) - float(amount)

def logout(name):
    print(f"Goodbye {name}")
