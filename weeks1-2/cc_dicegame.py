import random

high_score = 0


def dice_game(high_score):
    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    play = input("Enter your choice: ")
    
    while play != "1" and play != "2":
        print("That choice is invalid. Please enter 1 or 2.")
        print("\nCurrent High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        play = input("Enter your choice: ")
    while play != "2":
        def roll():
            range = [1,2,3,4,5,6]
            return random.choice(range)
        roll1 = roll()
        roll2 = roll()
        print("\nYou roll a...", roll1)
        print("You roll a...", roll2)
        total = roll1 + roll2
        print("\nYou have rolled a total of: " + str(total))
        if total > high_score:
            print("\nNew high score!")
            high_score = total
        print("\nCurrent High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        play = input("Enter your choice: ")
    if play == "2":
        print("Goodybye!")


dice_game(high_score)