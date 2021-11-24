from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin":"password123", "joe":"pw1"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if not authorized_user:
        print("You must be logged in to donate.")
    else: 
        print(f"Logged in as {authorized_user}")
    choice = input("Choose an option: ")
    if choice == "1":
        username = input("Enter Username: ").lower()
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        while True:
            username = input("Enter Username: ").lower()
            password = input("Enter Password: ")
            if len(username) <= 10 and len(password) >= 5:
                authorized_user = register(database, username)
                database[username] = password
                break
            else:
                print("Username cannot be more than 10 characters, and password must be at least 5 characters.")
        #print(database)

    elif choice == "3":
        if authorized_user:
            donation = donate(authorized_user)
            donations.append(donation)
        else:
            print("You are not logged in.")

    elif choice == "4":
        show_donations(donations)
        input("Press Enter to continue")

    elif choice == "5":
        #break
        exit()

print("Thanks for playing the donation game.")