import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    play = input(
        "Press enter to pick a card, or type Q then press enter to quit.")
    if play.lower() == "q":
        break
    card = random.choice(diamonds)
    print(card)
    hand.append(card)
    diamonds.remove(card)
    print(f"Remaining Cards: {diamonds}")
    print(f"Your hand: {hand}")

if not diamonds:
    print("There are no more cards to pick.")
