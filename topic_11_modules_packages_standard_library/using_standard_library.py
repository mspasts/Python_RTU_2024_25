# let's look into standard library
# if module is a single file
# then package is a directory with modules
# then library is a collection of packages

# Python comes with many built-in modules - standard library
# "Batteries included" philosophy

# full list of modules is here: https://docs.python.org/3/library/index.html

# let's start with simple strings module
# strings module provides some constants and functions for strings
# let's import it
import string
print("Punctuation:", string.punctuation) # note for some languages this might not be enough

# let's look at sys module
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter
import sys
# let's print current Python version
print("Python version:", sys.version)

# let's print the order of directories where Python looks for modules when importing
print("Path:", sys.path)

# this means that we do not want to call our modules sys.py or string.py or any other name that is already in use
# if you do so then you will not be able to import the system module

# let's import datatime from datetime module
from datetime import datetime # this is done because datetime is a class in datetime module
now = datetime.now() # so variable now has a fixed time that was taken here
print("Current date and time:", now)
# i can format the date and time
print("Formatted date and time:", now.strftime("%Y-%m-%d_%H:%M:%S")) # - : _ could be any character
for n in range(100_000):
    pass # do nothing 100_000 times
later = datetime.now()
print("It is now:", later)
print("Time taken:", later - now)
# i can also get out individual parts from datetime
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond) # one millionth of a second

# how about day of the week
# we could print number of the day of the week
print("Number of the day of the week:", now.strftime("%w")) # %w is for number of the day of the week
print("Day of the week:", now.strftime("%A")) # %A is for full name of the day

# we can add two datetime objects

# let's see what day of the week will be in 500 days
# for that we need timedelta class
from datetime import timedelta # this is done because timedelta is a class in datetime module
later = now + timedelta(days=500)
print("500 days from now will be:", later.strftime("%A"))
# print full date
print("500 days from now will be:", later)

# time and date can be tricky so use built-in modules!

# we already used Counter from collections module
from collections import Counter
# let's count letters in a string
c = Counter("hello")
print("Counter:", c)
# collections has some other useful classes such as defaultdict, namedtuple, deque, ChainMap, OrderedDict

# then we have math module which has some mathematical functions
import math
# let's calculate square root
print("Square root of 16:", math.sqrt(16)) # of course we could do 16 ** 0.5
# let's calculate factorial
print("Factorial of 5:", math.factorial(5)) # of course we could do 5 * 4 * 3 * 2 * 1
# let's calculate power
print("2 to the power of 3:", math.pow(2, 3)) # of course we could do 2 ** 3
# how about pi
print("Value of PI:", math.pi)
# there are many more functions in math module

# then we have random module
import random
# let's set a seed so we get pseudo-random numbers
random.seed(2024) # without seed the numbers would be different every time
# let's generate random number
print("Random number between 0 and 1:", random.random())
# we can simulate dice roll
print("Dice roll:", random.randint(1, 6)) # randint is inclusive - rare for Python
# insert xkcd joke about random numbers: https://xkcd.com/221/

# we can use random to shuffle a list
my_numbers = list(range(12))
print("Original list:", my_numbers)
shuffled_numbers = my_numbers.copy() # we need to copy the list because shuffle is in place
random.shuffle(shuffled_numbers) # IN PLACE
print("Shuffled list:", shuffled_numbers)

# shuffling is useful for games, Monte Carlo simulations, etc.
# better if you let the computer do the shuffling

# we can also choose some numbers from a list
print("Random choice from list:", random.choice(my_numbers))

# how about choosing multiple numbers ?
print("Random choices from list:", random.choices(my_numbers, k=3)) # k is how many numbers we want
# how about 12 numbers ?
saved_20 = random.choices(my_numbers, k=20)
print("Random choices from list:", saved_20) # with replacement meaning we can get the same number multiple times
# how about without replacement ?
print("Random choices from list:", random.sample(my_numbers, k=3)) # without replacement meaning we can get the same number only once
# then max for without replacement here would be 12 numbers
print("Random choices from list:", random.sample(my_numbers, k=12)) # without replacement meaning we can get the same number only once

# let's get some stats on saved_20

import statistics

print("Mean:", statistics.mean(saved_20))
print("Median:", statistics.median(saved_20))
print("Mode:", statistics.mode(saved_20)) # the most frequent number
# standard deviation
print("Standard deviation:", statistics.stdev(saved_20))
# there are external libraries for more advanced statistics

# next let's look at itertools module
import itertools

# let's look at permutations
# permutations are all possible orderings of elements
# order matters
letters = list("ABC")
print("Getting all permutations of ABC")
perms = itertools.permutations(letters)
print("Type of perms:", type(perms)) # this is not a list yet - it is a generator, similar to range
perms = list(perms) # now it is a list - fixed into memory
print("Permutations:", perms)
# number of Permutation is equal to n!
# n! = n * (n-1) * (n-2) * ... * 1
print("Permuation count:", math.factorial(len(letters)), len(perms))

# let's look at combinations
# combinations are all possible selections of elements
# order does not matter
# let's get 2 out of 3
print("Getting all combinations of ABC")
combs = itertools.combinations(letters, 2)
print("Type of combs:", type(combs)) # this is not a list yet - it is a generator, similar to range
combs = list(combs) # now it is a list - fixed into memory
print("Combinations:", combs)

# how about combinations with replacement - where we can get the same element multiple times
print("Getting all combinations with replacement of ABC")
combs_wr = itertools.combinations_with_replacement(letters, 2)
print("Type of combs_wr:", type(combs_wr)) # this is not a list yet - it is a generator, similar to range
combs_wr = list(combs_wr) # now it is a list - fixed into memory
print("Combinations with replacement:", combs_wr)

# how about when order matters ?
# we can use product
print("Getting all products of ABC")
prods = itertools.product(letters, repeat=2)
print("Type of prods:", type(prods)) # this is not a list yet - it is a generator, similar to range
prods = list(prods) # now it is a list - fixed into memory
print("Products:", prods)

# how about cartesian product  of two lists ?
# we can use product
print("Getting all cartesian products of ABC and 123")
prods = itertools.product(letters, "123")
print("Type of prods:", type(prods)) # this is not a list yet - it is a generator, similar to range
prods = list(prods) # now it is a list - fixed into memory
print("Cartesian Products:", prods)
# no need to write two nested loops

# how about cycling through a list multiple times ?
# we can use cycle
print("Cycling through ABCD 3 times")
letters = list("ABCD")
cycler = itertools.cycle(letters)
# cycler will cycle forever using next
for _ in range(3 * len(letters)):
    print(next(cycler), end=", ")

# this way I avoid creating a list with 3 copies of ABCD