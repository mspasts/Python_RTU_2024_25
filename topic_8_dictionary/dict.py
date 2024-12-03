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
# note that here adding a new key-value pair is the same as updating an existing key-value pair
# so if Edgars existed his value would be overwritten without warning
# if you want to add a new key-value pair only if key does not exist you should use setdefault method


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

# let's add Frank with same phone number as Bob
tel_dict["Frank"] = 112
# let's see dictionary again
print("Updated telephone dictionary:", tel_dict)

# the values could e anything for example a list, George has multiple phone numbers
tel_dict["George"] = [123, 456, 789] # only thing bad is that now data types are mixed
# so convienient but could be confusing
# let's see dictionary again
print("Updated telephone dictionary:", tel_dict)

# now how to get last phone number of George?
# first we get the list which is the value of George key
phone_list = tel_dict["George"]
# then we get the last element of the list
last_phone = phone_list[-1]
print("Last phone number of George:", last_phone)
# we could do this in one line
print("Last phone number of George:", tel_dict["George"][-1]) # other keys do not have lists as values only George

# we could delete George by key
# we could use del but we also have pop method
# pop method deletes the key-value pair and returns the value
george_phones = tel_dict.pop("George")
print("George's phone numbers:", george_phones)
# let's see dictionary again
print("Updated telephone dictionary:", tel_dict)

key_list = list(tel_dict.keys())
print("Keys in telephone dictionary:", key_list)
value_list = list(tel_dict.values())
print("Values in telephone dictionary:", value_list)

# lengths of both lists
print("Length of keys list:", len(key_list))
print("Length of values list:", len(value_list))

# let's recreate the same dictionary by giving the keys and values
# we could use zip function to combine the lists
also_dict = dict(zip(key_list, value_list))
# let's see dictionary again
print("Also telephone dictionary:", also_dict)
# length
print("Length of also telephone dictionary:", len(also_dict))

# we could reverse dictionary simply pass the values as keys and keys as values
reversed_dict = dict(zip(value_list, key_list))
# let's see dictionary again
print("Reversed telephone dictionary:", reversed_dict)
# length
print("Length of reversed telephone dictionary:", len(reversed_dict))
# we lose Bob! because both Bob and Frank used same phone number
# then Frank was added last as Value and so Bob is lost

# so we could decide to write a function that reverses the dictionary but keeps all the values
# so best would be that every key has a list of values, even single values are in a list

def reverse_dictionary(d):
    reversed_d = {} # so start with empty dictionary
    for key, value in d.items():
        if value not in reversed_d:
            reversed_d[value] = [key] #so create a list with key as first element
        else:
            reversed_d[value].append(key) # otherwise append key to the list
    return reversed_d

# let's see the reversed dictionary
reversed_dict = reverse_dictionary(tel_dict)
# let's see dictionary again
print("Reversed telephone dictionary:", reversed_dict)

# now how do I look up who has number 112?
# I just look up in the reversed dictionary
print("People with phone number 112:", reversed_dict[112])

# so notice the syntax for dictionaries is very similar to lists when using numbers as keys

# so when should you use dictionaries and when should you use lists when you have numbers as keys?

# if your indexes are continuous and start from 0 and go to n-1 then you should use lists
# example: top_ten_scores = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]

# if your indexes are all over the place and you need to look up values by keys then you should use dictionaries
# example big_num_dict = {100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"}
# would be silly to use list for this because we'd have so much wasted space

# again just like list using = will NOT COPY but create alias
tel_dict_alias = tel_dict
# so if I change tel_dict_alias I will change tel_dict
# but copy will create a new dictionary
tel_dict_copy = tel_dict.copy() # so backup dictionary

# let's see dictionary again
print("Telephone dictionary:", tel_dict)
print("Telephone dictionary alias:", tel_dict_alias)
print("Telephone dictionary copy:", tel_dict_copy)

# now let's change something in alias
# let's add Georgina with phone number 123
tel_dict_alias["Georgina"] = 123
print("*"*20)
# let's see dictionary again
print("Telephone dictionary:", tel_dict) # changed because alias
print("Telephone dictionary alias:", tel_dict_alias) # changed of course
print("Telephone dictionary copy:", tel_dict_copy) # not changed

# similary if I change something in copy
# for example let me clear it
tel_dict_copy.clear() # IN PLACE affects this data structure
# let's see dictionary again
print("*"*20)
print("Telephone dictionary:", tel_dict) # not changed
print("Telephone dictionary alias:", tel_dict_alias) # not changed
print("Telephone dictionary copy:", tel_dict_copy) # changed to empty dictionary

# one last thing when looping be careful when changing the dictionary keys (size)
# if you want to change keys you should create a new dictionary or loop through a copy
# let's make backup again
tel_dict_copy = tel_dict.copy()

# TOP DOWN approach
# let's see we want to go through a dictionary and remove all keys whose values are less than 9000
# so we could do this
for key in tel_dict.copy(): # so we loop through a copy
    if tel_dict[key] < 9000:
        del tel_dict[key] # this is bad because we are changing the dictionary size while looping

# let's see dictionary again
print("*"*20)
print("Telephone dictionary:", tel_dict) # changed
print("Telephone dictionary copy:", tel_dict_copy) # not changed

# the other way would be to build a dictionary with only the keys we want
# so GROUND UP approach
new_dict = {} # this is safe because we are not changing the size of the dictionary we are looping through
for key in tel_dict_copy: # no need for .copy() here because we are not changing the dictionary
    if tel_dict_copy[key] >= 9000:
        new_dict[key] = tel_dict_copy[key]

# let's see dictionary again
print("*"*20)
print("Telephone dictionary:", tel_dict) # not changed
print("Telephone dictionary copy:", tel_dict_copy) # not changed
print("New dictionary:", new_dict) # changed


# BONUS after break - look at dictionary comprehension - short way of creating dictionaries