import random

class GuessingGame():
    tries: int
    low: int
    high: int

    def __init__(self, tries, low, high):
        self.tries = tries
        self.low = low
        self.high = high
        self.answer = self.get_number()

    def get_number(self):
        return random.randint(self.low, self.high)
    
    def guess(self):
        attempts = self.tries
        print("Target",self.answer)
        while attempts > 0:
            print(f"{attempts} tries remaining")
            user_guess = int(input("Guess a number: "))
            if user_guess == self.answer:
                print("You guessed correctly!")
                return
            elif user_guess < self.answer: 
                print("Guess higher!")
            else: 
                print("Guess lower!")
            attempts -= 1
    def linear_guess(self):
        attempts = self.tries
        print("Target",self.answer)
        for i in range(self.low, self.high + 1):
            if attempts < 0:
                return
            print(f"{self.tries} tries remaining")
            user_guess = i
            print(i)
            if user_guess == self.answer:
                print("You guessed correctly!")
                return
            attempts -= 1

    def binary_search_guess(self):
        this_list = list(range(self.low,self.high+1))
        attempts = self.tries
        left = 0
        right = len(this_list) - 1
        print("Target",self.answer)
        while left <= right and attempts > 0:
            middle = (right + left) // 2
            potentialMatch = this_list[middle]
            print(middle)
            print(potentialMatch)
            if potentialMatch == self.answer:
                print("You guessed correctly!")
                return middle, potentialMatch
            elif potentialMatch > self.answer:
                right = middle-1  
            else:
                left = middle+1
            print(attempts)
            attempts -= 1



game = GuessingGame(5, 7, 15)
#game.guess()
#game.linear_guess()
game.binary_search_guess()