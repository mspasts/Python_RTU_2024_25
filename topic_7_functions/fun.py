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
    print("Result is", result) # this is not ideal to always print the result
    return result # here this local result will be returned and the name of the variable doesn't matter anywhere else

# let's test it
another_result = add_and_multiply(10, 20, 30)
print("Another result is", another_result)

# let's make a function that takes a list of numbers and returns the average
# this function actually exists in statistics module but let's make our own
# let's add verbose parameter to print the total and average
def avg(numbers, verbose=False): # so verbose is not required it will be False by default
    # verbose is just a parameter name that is commonly used, could be anything else legal for variable name
    total = sum(numbers)
    average = total / len(numbers)
    # so we have two local variables total and avg
    if verbose:
        print("Using verbose mode")
        print("Total is", total)
        print("Average is", average)
    return average

my_numbers = list(range(1, 11)) # so this is a list of numbers from 1 to 10
# let's test it
average = avg(my_numbers)
print("Average is", average)

more_numbers = list(range(1, 101))
# let's test it with verbose
average = avg(more_numbers, verbose=True)
print("Average is", average)

# i call default values "have your cake and eat it too" because you can use the function without specifying the parameter

# so if I know I will be using some common parameters, I can set them as default

# so you could all default values if you want in some function
# only requirment is that default values follow non-default values

# so what's different between parameters and arguments?
# in real life we use them interchangeably
# technically parameters are the names in the function definition
# arguments are the values we pass to the function

# now how about returning multiple values?
# we simply use , to separate them - technically we return a tuple - about those later

# let's make a function that returns min and avg and max of a list of numbers
# also we will use docstring to document the function
def min_avg_max(numbers):
    """
    Returns min, avg and max of a list of numbers
    Input: numbers - list of numbers
    Output: tuple of min, avg and max
    """

    # since we defined our own avg we can use it!
    return min(numbers), avg(numbers), max(numbers)

# let's test it - note how I can save all three values in one line
min_val, avg_val, max_val = min_avg_max(more_numbers)
print("Min is", min_val)
print("Avg is", avg_val)
print("Max is", max_val)

# one last thing - our functions in Python are pretty flexible
# they take pretty much any type of input arguments and return any type of output
# this can lead to some confusion and bugs

name = "Valdis "
food = "likes potatoes"
result = add(name, food) # will this work?
print("Result is", result) # what will be the result?

# Python has so called type hints that let us specify what type of input and output we expect
def add_with_type(a: int, b: int) -> int:
    """
    Adds two integers and returns the result
    Input: a - integer
    Input: b - integer
    Output: integer
    """
    return a + b

# let's test it
result = add_with_type(10, 20)
print("Result is", result)

# let's try with strings
str_result = add_with_type("Valdis", "likes potatoes")
print("String result is", str_result)

# turns out type hints in Python are like comments - they don't enforce anything
# so what's the use?
# they can be used by linters and IDEs to give you warnings and suggestions
# so you use them to catch bugs early and to document your code

# use type hints if you are writing code for others for sure!
# for yourself it depends on your style and how much you like to document your code