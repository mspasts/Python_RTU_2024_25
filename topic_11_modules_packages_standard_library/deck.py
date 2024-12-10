# let's make a card Deck class
# we will want a shuffle method
# we will want a peek method
# we will want a draw method - that will draw a card from the deck

import random

class Deck:
    def __init__(self, shuffle=False, seed=None):
        self.suits = ["kāravs", "ercens", "kreics", "pīķis"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = [(rank, suit) for rank in self.ranks for suit in self.suits]
        if seed: # without seed we will get different results each time we run the script
            random.seed(seed)
        if shuffle:
            self.shuffle()
        print("Jauns kāršu komplekts izveidots!")

    # let's make __str__ method that prints the deck
    def __str__(self):
        return str(self.deck) # we could think of some more formatted output
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def peek(self):
        return self.deck[-1]
    
    def draw(self):
        return self.deck.pop() # pop returns the last element of the list and removes it from the list
    


# let's test the class
if __name__ == "__main__":
    deck = Deck(shuffle=True, seed=42)
    print(deck.peek())
    print(deck.draw())
    print(deck.draw())
    print(deck)