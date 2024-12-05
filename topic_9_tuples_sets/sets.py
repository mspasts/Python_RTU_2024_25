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

# Finally we have set operations from set theory (kopu algebras)

# let's make a set of numbers from 0 to 9
numbers_0_9 = set(range(10))
print("Numbers from 0 to 9", numbers_0_9)

# i can also use {} to create a set
num_3_7 = {3, 4, 5, 6, 7, 7, 7, 3,4, 5, 6, 7} #if I have individual elements then I use {}
print("Numbers from 3 to 7", num_3_7)

# alternatively I could use set on a list
num_5_9 = set([5, 6, 7, 8, 9]) # if I have a sequence then I use set
print("Numbers from 5 to 9", num_5_9)

# let's start with checking some basic set operations
# subset - is one set contained in another
print("Is 3, 4, 5 a subset of 0 to 9?", {3, 4, 5}.issubset(numbers_0_9))
# is our num_3_7 a subset of numbers_0_9
print("Is 3 to 7 a subset of 0 to 9?", num_3_7.issubset(numbers_0_9))
# how about num_3_7 and num_5_9 ?
print("Is 3 to 7 a subset of 5 to 9?", num_3_7.issubset(num_5_9))

# we have a shorthand for subset - <=
# let's check 3 to 7 is a subset of 0 to 9
print("Is 3 to 7 a subset of 0 to 9?", num_3_7 <= numbers_0_9)
# we also have strict subset - <
# let's check 3 to 7 is a strict subset of 0 to 9
print("Is 3 to 7 a strict subset of 0 to 9?", num_3_7 < numbers_0_9)
# but if we check our numbers_0_9 is a subset of itself
print("Is 0 to 9 a subset of 0 to 9?", numbers_0_9 <= numbers_0_9)
# but it is not a strict subset
print("Is 0 to 9 a strict subset of 0 to 9?", numbers_0_9 < numbers_0_9)

# superset - is one set containing another
print("Is 0 to 9 a superset of 3 to 7?", numbers_0_9.issuperset(num_3_7))
# we have a shorthand for superset - >=
print("Is 0 to 9 a superset of 3 to 7?", numbers_0_9 >= num_3_7)
# we also have strict superset - >
print("Is 0 to 9 a strict superset of 3 to 7?", numbers_0_9 > num_3_7)
# but if we check our numbers_0_9 is a superset of itself
print("Is 0 to 9 a superset of 0 to 9?", numbers_0_9 >= numbers_0_9)
# but it is not a strict superset
print("Is 0 to 9 a strict superset of 0 to 9?", numbers_0_9 > numbers_0_9)

# disjoint - no elements in common
# let's check 3 to 7 and 5 to 9
print("Are 3 to 7 and 5 to 9 disjoint?", num_3_7.isdisjoint(num_5_9))

# union - all elements from both sets (no duplicates)
# union - Latviski apvienojums
# let's check 3 to 7 and 5 to 9 union
print("Union of 3 to 7 and 5 to 9", num_3_7.union(num_5_9))
# now let's check the shorthand it is | (pipe symbol)
# let's also save this
num_3_9 = num_3_7 | num_5_9 # so same as num_3_7.union(num_5_9)
print("Union of 3 to 7 and 5 to 9", num_3_9)
# union is a bit more forgiving thatn | in that it takes also other collections
all_kinds_set = num_3_7.union([10, 11, 12, 13], {14, 15, 16, 17}, "Valdis", ("Banana", "Apelsinš"))
print("Union of 3 to 7, 10 to 17", all_kinds_set)

# intersection - elements in common
# intersection - Latviski šķēlums
# let's check 3 to 7 and 5 to 9 intersection
print("Intersection of 3 to 7 and 5 to 9", num_3_7.intersection(num_5_9))
# now let's check the shorthand it is & (ampersand symbol)
# let's also save this
num_5_7 = num_3_7 & num_5_9 # so same as num_3_7.intersection(num_5_9)
print("Intersection of 3 to 7 and 5 to 9", num_5_7)
# careful with starting a intersection with an empty set
empty_set = set()
# let's check intersection with an empty set
print("Intersection of 3 to 7 and empty set", num_3_7.intersection(empty_set))
# we always get an empty set, because there are no elements in common

# difference - elements in one set but not in the other
# difference - Latviski atšķirība
# let's check 3 to 7 and 5 to 9 difference
print("Difference of 3 to 7 and 5 to 9", num_3_7.difference(num_5_9))
# now let's check the shorthand it is - (minus symbol)
# let's also save this
num_3_5 = num_3_7 - num_5_9 # so same as num_3_7.difference(num_5_9)
print("Difference of 3 to 7 and 5 to 9", num_3_5)
# note this is not symmetric
num_8_9 = num_5_9 - num_3_7
print("Difference of 5 to 9 and 3 to 7", num_8_9)

# finally we have symmetric difference - elements in one set or the other but not in both
# symmetric difference - Latviski simetriskā atšķirība
# let's check 3 to 7 and 5 to 9 symmetric difference
print("Symmetric difference of 3 to 7 and 5 to 9", num_3_7.symmetric_difference(num_5_9))
# now let's check the shorthand it is ^ (caret symbol)
# let's also save this
num_3_5_8_9 = num_3_7 ^ num_5_9 # so same as num_3_7.symmetric_difference(num_5_9)
print("Symmetric difference of 3 to 7 and 5 to 9", num_3_5_8_9)

# now union of differences should give you symmetric difference
# let's check
also_num_3_5_8_9 = num_3_5.union(num_8_9)
print("Symmetric difference of 3 to 7 and 5 to 9", also_num_3_5_8_9)

# i can compare sets for equality
# let's check if the sets have same elements
print("Are 3 to 7 and 5 to 9 equal?", num_3_7 == num_5_9)
# now lets compare those num_3_5_8_9 and also_num_3_5_8_9
print("Are 3 to 5, 8 to 9 and 3 to 5, 8 to 9 equal?", num_3_5_8_9 == also_num_3_5_8_9)

# again 3 major uses for sets
# 1. remove duplicates from a list
# 2. check for membership quickly in O(1) time
# 3. set operations from set theory - union, intersection, difference, symmetric difference, subset, superset, disjoint