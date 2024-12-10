# let's make a simple BlackJack game that uses our deck class

import random
from deck import Deck

class BlackJack:
    def __init__(self, shuffle=False, seed=None):
        self.deck = Deck(shuffle=shuffle, seed=seed)
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.game_over = False
        self.player_turn = True
        self.dealer_turn = False
        # if you think about it you only need one turn variable right?
        self.play()
    
    def play(self):
        self.player_hand.append(self.deck.draw())
        self.dealer_hand.append(self.deck.draw())
        self.player_hand.append(self.deck.draw())
        self.dealer_hand.append(self.deck.draw())
        self.calculate_score()
        self.print_game_state()
        while not self.game_over:
            if self.player_turn:
                self.player_turn = False
                self.player_play()
            if self.dealer_turn:
                self.dealer_turn = False
                self.dealer_play()
            self.calculate_score()
            self.print_game_state()
            self.check_game_over()
    
    def player_play(self):
        print("Player's turn!")
        print("Player's hand:", self.player_hand)
        print("Player's score:", self.player_score)
        if self.player_score < 21:
            choice = input("Do you want to draw another card? (y/n): ")
            if choice == "y":
                self.player_hand.append(self.deck.draw())
                self.player_turn = True
            else:
                self.dealer_turn = True
        else:
            self.game_over = True
            print("Player has lost!")
    
    def dealer_play(self):
        print("Dealer's turn!")
        print("Dealer's hand:", self.dealer_hand)
        print("Dealer's score:", self.dealer_score)
        if self.dealer_score < 17: # here we could implement some other strategy
            self.dealer_hand.append(self.deck.draw())
            self.dealer_turn = True
        else:
            self.game_over = True
            print("Dealer has lost!")
    
    def calculate_score(self):
        self.player_score = self.score(self.player_hand)
        self.dealer_score = self.score(self.dealer_hand)
    
    def score(self, hand):
        score = 0
        aces = 0
        # TODO add extra logic to fix the aces
        # if the score is over 21 and there are aces in the hand
        # we should change the value of the ace from 11 to 1
        # and recalculate the score
        # consult official rules of blackjack
        for card in hand:
            rank = card[0] # so we only care about the rank
            # we do not need suit which is card[1]
            # here we can see how one improvement would be Card class
            # then we could see immediately which properties we have
            if rank in ["J", "Q", "K"]:
                score += 10
            elif rank == "A":
                aces += 1
            else:
                score += int(rank)
        for _ in range(aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        # FIXME this is not 100% correct for hand with two Aces it could be 2 or 12
        return score
    
    def print_game_state(self):
        print("Player's hand:", self.player_hand)
        print("Player's score:", self.player_score)
        print("Dealer's hand:", self.dealer_hand)
        print("Dealer's score:", self.dealer_score)

    def check_game_over(self):
        if self.player_score > 21:
            self.game_over = True
            print("Player has lost!")
        elif self.dealer_score > 21:
            self.game_over = True
            print("Dealer has lost!")
        elif self.player_score == 21:
            self.game_over = True
            print("Player has won!")
        elif self.dealer_score == 21:
            self.game_over = True
            print("Dealer has won!")
        elif len(self.deck.deck) == 0:
            self.game_over = True
            print("No more cards in the deck!")
        # we could add more checks here

if __name__ == "__main__":
    print("Let's play BlackJack!")
    game = BlackJack(shuffle=True, seed=42)
    game.play()

# FIXME looks like the dealer draw two cards at the end of the game even when losing
# also we could add more checks for the game over
