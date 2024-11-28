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

# order_food()

# now I can call the function
# order_food() # note the parentheses

# # i could call it 5 times
# for _ in range(5):
#     order_food()



# let's make a function called order_any
def order_any(food): # so food is a parameter
    walk_to_restaurant()
    print(f"Order {food}")

# order_any("pizza")

# let's make a function that a list of foods and orders all of them
def order_all(foods):
    print(f"Let's order {len(foods)} food items")
    for food in foods:
        order_any(food)
    print("All food ordered")

# print("About to order")

# I can give a list of foods directly
# order_all(["pizza", "burger", "fries"])

# i can save the list of foods in a variable and then pass it
health_foods = ["salad", "grilled chicken", "water"]
# order_all(health_foods)

# print("Done")

# let's make a function that prints addition of two numbers
# so to use more parameters, we just add them in the parentheses
# we separate parameters with commas
def print_add(a, b):
    print(a + b)
    # we could do more here

# let's test it
print_add(1, 2)
print_add(50, -5)

# so this print_add function works
# but it has a minus that it doesn't return the value
# it just prints it - so called side effect
# functions should ideally return values and not have side effects
# of course printing is a useful side effect, but it's not always what we want

# let's try saving the result of print_add
result = print_add(5, 6)
print("Result is", result) # None - because print_add doesn't return anything

print("None is what is returned when a function doesn't return anything")
# note None is returned by print function too

# so how do we rectify this?
# we use the return keyword
def add(a, b):
    return a + b

# now we can save the result of a function that returns a value
my_result = add(10, 20)
print("My result is", my_result)
# i can reuse the result now!

# let's make a slightly more complex function
def add_and_multiply(a, b, c):
    # we will create a local to the function variable called result
    # this local result is not related to the global result variable outside the function
    result = (a + b) * c # note this result is local to the function
    print("Result is", result)
    return result # here this local result will be returned and the name of the variable doesn't matter anywhere else

# let's test it
another_result = add_and_multiply(10, 20, 30)
print("Another result is", another_result)