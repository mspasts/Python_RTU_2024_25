# Let's talk about sets (kopa Latviski)
# Sets are unordered collections of unique elements
# mutable - we can add and remove elements
# we can't access elements by index
# we can check membership of an element VERY QUICKLY just like checking for key in dictionary
# we also have set operations like union, intersection, difference

# official Python tutorial: https://docs.python.org/3/tutorial/datastructures.html#sets
# real-python: https://realpython.com/python-sets/

# we can create a set from strings
char_set = set("abracadabra")
print(char_set) # note that duplicates are removed
# note that order is not preserved, it is an unordered collection
# the order is not guaranteed to be the same as the order of insertion
# we can get length
print("Length of the set", len(char_set))

# we can check for membership VERY QUICKLY unlike lists or tuples
print('Is "a" in the set?', "a" in char_set)
print('Is "z" in the set?', "z" in char_set)

# how would I get a string of unique characters from a string?
# we have the unique characters in the set already
# let's sort them and join them into a string
unique_chars = sorted(char_set) # list of unique characters
print("Unique characters", unique_chars)
# now we can join them into a string
unique_string = "".join(unique_chars) # I join them with no separator to get a string
print("Unique string", unique_string)

# so now we see how we can start with some list and get a different list with unique elements

shopping_list = ["milk", "bread", "butter", "milk", "bread", "butter", "milk", "bread", "butter"]
print("Shopping list", shopping_list)
# we can convert this list to a set
unique_shopping_set = set(shopping_list)
print("Unique shopping set", unique_shopping_set)
# now we can go down to a list again
unique_shopping_list = list(unique_shopping_set) #if i wanted ordered list I would use sorted here
print("Unique shopping as a list", unique_shopping_list)
# of course I could sort later
sorted_unique_shopping_list = sorted(unique_shopping_list) # sorted takes time, so if I don't need it, I don't use it
print("Sorted unique shopping list", sorted_unique_shopping_list)

# i can loop through a set if I want to
print("Looping through the set")
for item in unique_shopping_set:
    print(item)

# we can add elements to a set
unique_shopping_set.add("eggs")
print("Unique shopping set after adding eggs", unique_shopping_set)
# let's try adding bread again
unique_shopping_set.add("bread") # no error, but bread is not added
print("Unique shopping set after adding bread again", unique_shopping_set)

# now I can also remove elements
unique_shopping_set.remove("milk")
print("Unique shopping set after removing milk", unique_shopping_set)
# removing an element that is not in the set will raise an error
try:
    unique_shopping_set.remove("milk")
except KeyError as e:
    print("Error removing milk", e)

# if I did not want to use try I could use if to check if the element is in the set
if "milk" in unique_shopping_set: # very quick operation
    unique_shopping_set.remove("milk")
else:
    print("Milk is not in the set")