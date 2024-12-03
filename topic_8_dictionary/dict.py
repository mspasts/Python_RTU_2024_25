# mēs zinam par sarakstiem, kas glabā vairākus elementus kaut kādā secībā
# so we know about lists that store multiple elements in some order
# lists are great if you want to store multiple elements in a specific order
# the disadvantage of lists is that they are not very good for searching for elements
# if I have a list of million elements and I want to find a specific element, I have to go through all the elements

# instead dictionaries are great for searching for elements
# dictionaries let us store key-value pairs
# Latviski: vārdnīcas ļauj mums glabāt atslēgu-vērtību pārus

# in other programming languages dictionaries are called maps, associative arrays, or hash maps

# the main idea is that we can "instantly" find a value by its key - computer science calls this O(1) time complexity
# so no matter how large our dictionary is, we can find a value by its key in the same amount of time
# even if I have million key - value pairs I can still find a value by its key in the same amount of time
# similarly I can add a new key-value pair in the same amount of time and delete a key-value pair in the same amount of time

# some properties of dictionaries:
# 1. dictionaries are enclosed in curly braces {}
# 2. dictionaries store key-value pairs
# 3. keys are unique - values can be repeated
# 4. keys can be strings, numbers, or tuples
# 5. values can be any data type
# 6. dictionaries are mutable - we can change the values and keys
# 7. dictionaries are unordered - the order of the elements is not guaranteed 
# Technically Python preserves the order of the elements in the dictionary since 3.6
# There are ordered dictionaries in Python - OrderedDict but those are slower than regular dictionaries
# 8. dictionaries are iterable - we can loop through the keys, values, or key-value
# 9. dictionaries can be nested - we can have dictionaries inside dictionaries

# so let's start with an empty dictionary
empty_dict = {} # typical way to create an empty dictionary
# could use also dict() function
also_empty_dict = dict()
# dict() can be used to create a dictionary from a list of tuples

print("Empty dictionary:", empty_dict)
print("Also empty dictionary:", also_empty_dict)

# let's check the length of the dictionary
print("Length of empty dictionary:", len(empty_dict))

# let's create a dictionary with some key-value pairs - in this case some phone numbers

tel_dict = {"Alice": 123456, "Bob": 654321, "Charlie": 987654, "David": 456789}

print("Telephone dictionary:", tel_dict)

# length
print("Length of telephone dictionary:", len(tel_dict))

# find value by key
# main use is to get value using key
# so let's get Alice's phone number
print("Alice's phone number:", tel_dict["Alice"]) # so this is very fast - O(1) time complexity

# second thing we might want to add a new key-value pair
# let's add Edgar's phone number
tel_dict["Edgars"] = 147258 # again this is O(1) time complexity - VERY FAST even on large dictionaries
# compare with list where appending an element is O(1) but inserting an element somewhere is slower - O(n) time complexity

# stats on our dictionary
print("Updated telephone dictionary:", tel_dict)
print("Length of updated telephone dictionary:", len(tel_dict))

# similarly we can delete a key-value pair in O(1) time complexity - VERY QUICKLY
# let's get rid of Bob's phone number
del tel_dict["Bob"]

# stats again
print("Updated telephone dictionary:", tel_dict)
print("Length of updated telephone dictionary:", len(tel_dict))

# what happens if i try to del non-existing key
# we get KeyError
try:
    del tel_dict["Bob"]
except KeyError as e:
    print("KeyError:", e)

# we could first check if the key exists
# so called membership test - this is VERY FAST as well - O(1) time complexity
if "Bob" in tel_dict:
    print("Goodbye Bob")
    del tel_dict["Bob"]
else:
    print("Bob is already gone")

# similarly what happens if I want to get Bob's phone number and he is not in the dictionary?
# we get key error
try:
    print("Bob's phone number:", tel_dict["Bob"])
except KeyError as e:
    print("KeyError:", e) 

# we could use in to check first
# note in is faster than checking for something in a list

if "Bob" in tel_dict:
    print("Bob's phone number:", tel_dict["Bob"])
else:
    print("Sorry Bob is not in the dictionary")

# if this is common operation we could use get method
alice_phone = tel_dict.get("Alice")
print("Alice's phone number:", alice_phone)
bob_phone = tel_dict.get("Bob")
print("Bob's phone number:", bob_phone) # returns None if key is not in the dictionary
default_phone = tel_dict.get("Bob", 1188) # so if I supply 2nd argument it will return that if key is not in the dictionary
print("default phone number:", default_phone)

# let's add a default value for Bob
tel_dict.setdefault("Bob", 112) # this works only if key is not in the dictionary
print("Updated telephone dictionary:", tel_dict)
# bob is back but note he is now in the end of the dictionary
# now if I try setdefault again it will not change the value
tel_dict.setdefault("Bob", 113) # this works only if key is not in the dictionary
print("Updated telephone dictionary:", tel_dict)
# so setdefault is useful if you want to add a default value only if key is not in the dictionary
# it is equivalent to following code
if "Bob" not in tel_dict: # very fast
    tel_dict["Bob"] = 114

# so let's see dictionary again
print("Updated telephone dictionary:", tel_dict)

# we do not need to use literal strings for keys we can use variables
name = "Charlie" # also could call this needle, or key, or anything else
print(name + "'s phone number:", tel_dict[name])

# let's loop through our dictionary

# first let's loop through the keys

print("Keys in telephone dictionary:")
for key in tel_dict:
    print(f"KEY -> {key}, VALUE -> {tel_dict[key]} == {tel_dict.get(key)}")
    # the get here is not needed
    # why?
    # because looping through the dictionary gives us the keys guaranteed
    # so a tiny bit slower to use get here because it includes if to check if key is in the dictionary

# we also have a way to go through keys and values
# this is useful if we need both key and value
print("Keys and values in telephone dictionary:")
for key, value in tel_dict.items(): # of course could use any variable names here, k,v for example
    print(f"KEY -> {key}, VALUE -> {value} == {tel_dict[key]}")
