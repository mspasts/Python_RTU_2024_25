# it can be convenient to create dictionaries using shorter syntax
# syntax is:
# {key: value for key, value in iterable}

# we could create a dictionary that doubles existing values
some_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 5, 'e': 6}
# so to double the values we can use a dictionary comprehension
# we go through all key-value pairs in the original dictionary
# and create a new dictionary with the same keys but doubled values
double_dict = {key: value * 2 for key, value in some_dict.items()}
print(double_dict)

# the iterable can be a simple list or string

# let's create a dictionary of characters and their Unicode values

some_string = "Python is sometimes easy - dažreiz grūts 😁"

# we can use a string as an iterable
# so we go through all characters in the string
# and create a dictionary with characters as keys and Unicode values as values

char_dict = {char: ord(char) for char in some_string}
print(char_dict)

# i can also set up fixed value for values for example 0 for counting something

food_list = ['apple', 'banana', 'carrot', 'donut', 'egg', 'fish', 'grape', 'honey', 'ice cream', 'jelly']

# let's create a dictionary with food items as keys and 0 as values
# so we go through all food items in the list
# and create a dictionary with food items as keys and 0 as values
food_dict = {food: 0 for food in food_list} # instead of 0 I could have used whatever value I wanted
print(food_dict)

# I could also add a filter similar to list comprehensions

# let's filter the above dictionary for food items that start with a vowel
# so we go through all food items food_dict
# and create a dictionary with food items that start with a vowel as keys and 0 as values
vowel_food_dict = {food: counter+5 for food, counter in food_dict.items() if food[0].lower() in 'aeiou'}
print(vowel_food_dict)

# again this is a convenience you can always do the same thing with the following code
new_dict = {}
for food, counter in food_dict.items():
    if food[0].lower() in 'aeiou':
        new_dict[food] = counter + 5 # of course 5 is arbitrary could be any number
print(new_dict)

# so dictionary comprehension is for simpler filters or modification
# dictionary comprehension is always OUT OF PLACE - it creates a new dictionary!

