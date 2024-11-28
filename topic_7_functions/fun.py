# functions let us organize our code into reusable blocks
# philosphy: DRY - Don't Repeat Yourself
# functions should do one thing and do it well - not always possible, but a good goal
# functions let us abstract away complexity

# let's say I want to go eat and order food
# i could write instruction with print
# print("Walk to the restaurant")
# print("Open the door")
# print("Walk to the counter")
# print("Look at the menu")
# print("Order food")
# what if I have to do it again?
# i'd have to copy and paste the instructions... what if I make a mistake?

# let's make a function that walks to the restaurant and its counter
def walk_to_restaurant():
    print("Walk to the restaurant")
    print("Open the door")
    print("Walk to the counter")
    print("Look at the menu")


# let's make a function to order food
def order_food(): # note blank parentheses and colon
    # here I write the instructions
    walk_to_restaurant()
    print("Order good food")

order_food()

# now I can call the function
# order_food() # note the parentheses

# # i could call it 5 times
# for _ in range(5):
#     order_food()



# let's make a function called order_any
def order_any(food): # so food is a parameter
    walk_to_restaurant()
    print(f"Order {food}")

order_any("pizza")