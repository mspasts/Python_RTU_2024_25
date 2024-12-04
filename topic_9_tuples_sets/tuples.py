# let's talk about Python tuples - korteži Latviski
# Essentially tuples are immutable lists
# there are some similarities with strings which similarly are immutable

# Usage for passing data around that you don't want to be changed
# Tuples are faster than lists, but they cannot be changed
# "Safer" to use than lists, because you can't accidentally change the data
# Size is fixed, so you can't add or remove elements
# We will see that it is possible to mutate some data inside a tuple - but those are rare cases
# Tuples can be used as KEYS in dictionaries, while lists cannot

# Philosophically, tuples are used for fixed collections of items
# Heterogeneous data - different types of data
# IF we have a large collection of homogeneous data, list would be more appropriate

# more in real-python: https://realpython.com/python-lists-tuples/

# so we create a tuple with round brackets ()

# empty tuple - why would you want this?
empty_tuple = ()
print("Type of data", type(empty_tuple))
# length of the tuple
print("Length of the tuple", len(empty_tuple))
# we might use Empty tuple sometimes as a placeholder, or to pass a value to function
# also maybe we want a default value for a function, that is a container

# tuple with one element - again if you want to pass a single value to a function that expects a tuple
# you need to add a comma after the value
single_element_tuple = (100,) # note the comma otherwise it will be treated as an integer
print("Type of data", type(single_element_tuple))
print("Length of the tuple", len(single_element_tuple))

# let's make a normal tuple about Alice and her age, occupation and salary, hobbies
# we can have different types of data in a tuple
alice = ("Alice", 25, "Programmer", 1000.75, ["reading", "running"])
print("Type of data", type(alice))
print("Length of the tuple", len(alice))

number_tuple = tuple(range(0,100, 10))
# note also use of tuple to conver some other collection to a tuple
# we can use tuple on list, string, range and other collections
print("Type of data", type(number_tuple))
print(number_tuple)
print("Length of the tuple", len(number_tuple))

# so indexing works just like regular lists
print(alice[0])
print(alice[1])
# last element using negative index
print(alice[-1])

# for slicing let's slice number_tuple using same type of syntax as for lists,string etc
print(number_tuple[2:5]) # so from 3rd to 5th element, essentially indexes 2,3,4
# first 4 elements
print(number_tuple[:4]) # 0 is default start
# last 4 elements
print(number_tuple[-4:]) # end element is included
# note that is not the same as
print(number_tuple[-4:-1]) # last element is NOT included

reversed_tuple = number_tuple[::-1] # same trick as with lists
# also note if we do not save the result, the original tuple is not changed
print("Original tuple", number_tuple)
print("Reversed tuple", reversed_tuple)

# turns out we do not need parenthesis for tuples size 2 and more
# we can just use commas
bob = "Bob", 30, "Teacher", 800.50, ["swimming", "cooking"]
print("Type of data", type(bob))
print("Length of the tuple", len(bob))

# so now we can see how we return multiple values from a function
# we can return a tuple, and then we can unpack it
def get_min_sum_max(numbers):
    return min(numbers), sum(numbers), max(numbers) # could use parenthesis, but not necessary

# now we can utilize the function
my_min, my_sum, my_max = get_min_sum_max(number_tuple)
print("Min", my_min)
print("Sum", my_sum)
print("Max", my_max)

# we also just used tuple unpacking - meaning we get a tuple from a function, and we unpack it

# instead we could have gotten a tuple and unpacked it later
result_tuple = get_min_sum_max(number_tuple)
print("Tuple result", result_tuple)
# unpacking later
my_min, my_sum, my_max = result_tuple
print("Min", my_min)
print("Sum", my_sum)
print("Max", my_max)

# note unpacking works on lists as well

# we can also pack the values into a tuple could be variables or literals
# results_packed = (my_min, my_sum, my_max) # parenthesis are optional
results_packed = my_min, my_sum, my_max
print("Packed results", results_packed)

# we can also use tuple unpacking to swap values
year_a = 2020
year_b = 2024
print("Before swap", year_a, year_b)

year_a, year_b = year_b, year_a # this is evaluated as a tuple then unpacked # so right side is a tuple

print("After swap", year_a, year_b)

# if I did not have this unpacking, I would need a temporary variable
# temp = year_a
# year_a = year_b
# year_b = temp
# we could do it with multiple values not only 2

# let's first assign a,b,c,d values
a, b, c, d = 1, 2, 3, 4 # so we create a tuple and then unpack it
print(a, b, c, d)
# now let's reverse the values
a, b, c, d = d, c, b, a # so we create a tuple and then unpack it
print(a, b, c, d)

# now if we are unpacking a larger tuple, we can use * to capture the rest of the values

# so let's capture head and tail of a tuple and leave middle values
head, second, *middle, tail = number_tuple # so number_tuple should be list or tuple
# instead
print("Number tuple", number_tuple)
print("Head", head)
print("Second", second)
print("Middle", middle) # note that *middle is a list not tuple
print("Tail", tail)

# of course I could have done it as follows
head = number_tuple[0]
second = number_tuple[1]
middle = number_tuple[2:-1] # here I would get tuple
tail = number_tuple[-1]
print("Number tuple", number_tuple)
print("Head", head)
print("Second", second)
print("Middle", middle) # note that *middle is a list not tuple
print("Tail", tail)

# so dictionary items gives us something like list of tuples
my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
print(my_dictionary.items())
list_tuples = list(my_dictionary.items())
print(list_tuples)

# lastly we can use tuples as keys in dictionaries
charles = "Charles", 33, 180
# we can use charles as key in a dictionary
# however alice and bob will not work as keys because they have lists inside
# people = {alice: "Alice", bob: "Bob", charles: "Charles"} # this will not work
people = {charles: "Charles", ("Bob", "Builder"): "Bobiņš"}
print(people)
print("Keys", people.keys())
print("Values", people.values())
# look up Bob
print(people[("Bob", "Builder")])
# we could use this approach if we want to have a keys in a dictionary say of first name and last name

# there are also something called NamedTuples, which are like tuples but with named fields - some other time
# also we could start using some Object Oriented Programming and create classes with attributes
