donations_sum = 0

def show_homepage() :
    print("      === DonateMe Homepage ===      ")
    print("-------------------------------------")
    print("|1.  Login       |    2. Register   |")
    print("-------------------------------------")
    print("|3.  Donate      | 4. Show Donations|")
    print("-------------------------------------")
    print("|               5. Exit             |")
    print("-------------------------------------")

def donate(username):
    donation_amount = float(input("How much would you like to donate?"))
    global donations_sum 
    donations_sum += donation_amount
    donation = f"{username} has donated ${donation_amount:.2f}"
    print(f"Thank you for your donation.")
    return donation

def show_donations(donations):
    print("\n --- All donations ---")
    if len(donations) < 1:
        print("Currently there are no donations. Please donate!")
    else:
        for donation in donations:
            print(donation)
            print("Total", donations_sum)