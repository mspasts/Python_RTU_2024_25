import random

# Funkcija, kas izveido kāršu komplektu un sajauc to "in-place"
def get_shuffled_cards():
    # Definējam kāršu mastus un kārtis
    suits = ["kāravs", "ercens", "kreics", "pīķis"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    # Veidojam kāršu komplektu (tuple ar katru kārti un tās mastu)
    deck = [(rank, suit) for rank in ranks for suit in suits] # this is double list comprehension
    
    # Sajaucam kāršu komplektu "in-place"
    random.shuffle(deck)
    
    return deck
 
# Funkcija, kas atgriež patvaļīgu kārti no sajauktās virknes
def draw_random_card(deck):
    return random.choice(deck)
 
# Funkcija, kas atgriež jaunu sajauktu virkni (out of place)
def get_shuffled_cards_out_of_place():
    suits = ["kāravs", "ercens", "kreics", "pīķis"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    deck = [(rank, suit) for rank in ranks for suit in suits]
    
    # Atgriež jauniem sajauktiem kārtīm
    return random.sample(deck, len(deck))
 
# Pārbaudīsim funkcionalitāti
 
# Izveidojam sajauktu kāršu komplektu
shuffled_deck = get_shuffled_cards()
print("Sajaukts kāršu komplekts (in-place):")
print(shuffled_deck)
 
# Izvēlamies patvaļīgu kārti no sajaukta komplekta
random_card = draw_random_card(shuffled_deck)
print(f"\nPatvaļīgi izvēlēta kārts: {random_card}")
 
# Izveidojam jauniem sajauktu kāršu komplektu (out of place)
shuffled_deck_out_of_place = get_shuffled_cards_out_of_place()
print("\nJauns sajaukts kāršu komplekts (out-of-place):")
print(shuffled_deck_out_of_place)