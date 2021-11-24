def login(database, username, password) :
    if (username, password) in database.items():
        print(f"Welcome {username}!")
        return username
    elif username not in database.keys():
        print("User not found please register.")
        return ""
    else:
        print("Incorrect password for user.")
        return ""
    
def register(database, username):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        print(f"Username {username} registered. ")
        return username