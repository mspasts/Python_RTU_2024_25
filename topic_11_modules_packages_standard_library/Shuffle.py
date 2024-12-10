import random

def shuffled_cards():
    tipi = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    mastis = ["kāravs","ercens","kreics","pīķis"]
    
    kava = [(r, s) for r in tipi for s in mastis]
    
    random.shuffle(kava)
    return kava

cards = shuffled_cards()
print(cards)

random_card = random.choice(cards)
print(random_card)

def get_out_of_place_shuffled_cards():
    tipi = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    mastis = ["kāravs","ercens","kreics","pīķis"]
    kava = [(r, s) for r in tipi for s in mastis]
    return random.sample(kava, len(kava))

new_cards = get_out_of_place_shuffled_cards()
print(new_cards)
