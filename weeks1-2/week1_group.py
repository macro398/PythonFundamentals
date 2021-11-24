wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

wiz_hp = 70
elf_hp = 100
human_hp = 150

wiz_dmg = 150
elf_dmg = 100
human_dmg = 20

while True:
    dragon_hp = 300
    dragon_dmg = 50
    while True:
        print("Choose your character!")
        print(f"Input 1 or type wizard for {wizard}")
        print(f"Input 2 or type elf for {elf}")
        print(f"Input 3 or type human for {human}")
        carSelect = input("Choose your character : ").lower().strip()

        if carSelect == "1" or carSelect == "wizard":
            character = wizard
            myhp = wiz_hp
            mydmg = wiz_dmg
            break
        if carSelect == "2" or carSelect == "elf":
            character = elf
            myhp = elf_hp
            mydmg = elf_dmg
            break
        if carSelect == "3" or carSelect == "human":
            character = human
            myhp = human_hp
            mydmg = human_dmg
            break
        if carSelect == "4" or carSelect == "dragon":
            character = dragon
            myhp = dragon_hp
            mydmg = dragon_dmg
            break

        if carSelect == "quit":
            character = carSelect
            playAgain = "no"
            break
        print("Unknown character")

    if character != carSelect:
        print(
            f"You have selected the {character} character. Your character has {myhp} hit points and deals {mydmg} damage.")

    # Task 4: Battle Phase
    if character != dragon and character != "quit":
        while True:
            dragon_hp = dragon_hp - mydmg
            print(
                f"You hit the dragon for {mydmg} damage, the dragon has {dragon_hp} hp remaining")
            if dragon_hp <= 0:
                print("The dragon has been defeated!")
                break
            myhp = myhp - dragon_dmg
            print(
                f"The dragon hits you for {dragon_dmg} damage, you have {myhp} hp remaining")
            if myhp <= 0:
                print("You have been defeated. Better luck next time!")
                break

    if character == dragon and character != "quit":
        print(
            f"You cheated, you weren't supposed to select {dragon}! Enjoy the endless while loop, sucker.")
        while True:
            print("Cheating is bad!")

    while True and playAgain != "no":

        playAgain = input(
            "Would you like to play again? Yes/No : ").lower().strip()
        if playAgain == "no":
            break
        if playAgain != "yes" and playAgain != "no":
            print("That is not a yes or no...")
        if playAgain == "yes":
            break

    if playAgain == "no":
        break
