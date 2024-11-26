# string is a sequence (ordered collection)
# of single letter strings in Python

# Python strings are immutable
# means we do not change them - we can overwrite
# but we do not change individual characters in same string
# instead when we modify string we create a new one

food = "Sushi"
# in Python no difference between " and ' for string
drink = 'Green Tee'
print(food, drink)
# so if i want ' inside I use " outside
quoted_text = "It's a sunny day, isn't it?"
print(quoted_text)

another_quote = 'It is a "sunny" day indeed today'
print(another_quote)

# so if I need both
# I have a couple of choices
# I could use so called escape characters
# all escape chars: https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

escaped_text = "some text with \"quote\" also normal 'quote' inside"
print(escaped_text)

#if i need \ in the text I can use \\ - this is ONE \
more_escaped_text = "some backslash \\ and newlines\n\n\n and tab\t\t\taha"
print(more_escaped_text)

# we also have raw strings no escape allowed!
raw_text = r"double backslash \\ or \n \t or anything \ really"
print(raw_text)
# r"text" is good for things like regular expressions which need more escaping

# we also have so called multiline strings
# starts and ends with """ or '''
multi_line_string = """Rakstu ko gribu,
\tlasu ko gribu,
\tdziedu ko gribu,
ēdu ko gribu,
dzeru, ko gribu

Un tad "skrienu", kur gribu"""

print(multi_line_string)

name = "Valdis"
food = "potatoes 🥔"
drink = "kefir"
# i can use multiline strings together with f strings
string_template = f""" I am {name} I love {food}
Also I like to drink {drink}.
Life is good!"""
print(string_template)

# Indexing - accessing individual items in a collection - string
food = "kartupelis"

# first letter - index starts with 0!
print("First letter of food is", food[0])
print("Second letter of ", food, "is", food[1])
print("Third letter of ", food, "is", food[2])

print("Tenth letter of food", food, "is", food[9])
# not 10th?
try:
    print(food[10])
except IndexError as e:
    print("Sorry", e)
    
print("How many letters in ", food, "?", len(food))

# so last letter could be done the following way...
print("Last letter of any string", food[len(food)-1]) # not Pythonic!!!
# no need
# Python offers 2nd indexing - starts from end and goes from -1 until -len
print("Last letter of any string", food[-1]) # last item
print("2nd to last", food[-2])
# middle easy
middle_index = len(food) // 2
print("Around middle", food[middle_index-1],food[middle_index]) # so 5 meaning 6th

# Python offers a great standard way to get substrings - or slices
# best thing since sliced bread...
# so let's get first 3 letters of kartupelis
# full syntax would be
print("First three letters of food", food[0:3])
# 0 is not required
print("First three letters of food", food[:3])
print("2nd and 3rd letter of food", food[1:3])
print("4th and to the end", food[3:]) # so : after is end of the string
print("4th,5th,6th", food[3:6]) # so : after is end of the string

# last 3 letters
print("Last 3 letters", food[-3:])
print("Last 5 letters", food[-5:])

# unlike index, Slice lets you use any number...

print("Last 5 letters", food[-5:964564]) # same as [-5:] as long as we
# have less than 964564 letters...
# i could go overshoot the other way as well
print("full string", food[-414323:35252])

import string # for alphabet # these are some values
alphabet = string.ascii_lowercase
print(alphabet)
print("English alphabet has", len(alphabet), "characters")

# we can use steps in slicing
print("Every second letter", alphabet[::2]) # so first two default to start and end
print("Every second letter start at second", alphabet[1::2]) # so first two default to start and end
print("start at 3rd, jump every 4th and end at 13th", alphabet[2:13:4])

# how to reverse a string the Python way
reverse_string = alphabet[::-1]
print("reverse alphabet", reverse_string)

# again loop
for c in food:
    print("Working on letter", c)
    
# existance check whether string has something
# works on other collections too!
print("is p in food?", "p" in food)
# we can use a generic term for variable such as needle
needle = "art"
print("is our search term in our target?", needle in food)
print(f"is {needle} in {food} ? {needle in food}")

# we can find the first occurance of search string
print("where does p first occur in food?", food.index("p"))
print("where does p first occur in food?", food.find("p"))
# what is the difference?
# index will throw error, find will return -1 on not finding
bad_needle = "pele"
print("is bad_needle in food?", bad_needle in food)
print("find bad_needle in food?", food.find(bad_needle)) # -1
try:
    print("index of bad_needle in food?", food.index(bad_needle)) # error
except ValueError as e:
    print("Sorry", e)
    
# now how about changing strings?
# we can not change directly strings in Python
try:
    food[5] = "m"
except TypeError as e:
    print("oops", e)

# what to do?
# we have some options
# all involve making a new string
# replace all
new_food = food.replace("p", "m")
print(new_food)
breakfast= "Auzu putra ar mellenēm"
# let's change u to y
new_breakfast = breakfast.replace("u", "y")
print(new_breakfast)
another_breakfast = breakfast.replace("u", "y", 2) # 2 means replace first 2
print(another_breakfast)

# i could also rebuild a string
also_food = food[:5]+"m"+food[6:] # so first 5 then put 6th as new "m" then 7th and on
print(also_food)
# could use f-strings
and_food = f"{food[:5]}mmmmmmMmm{food[3:]}"
print(and_food)
# let's try with slices
tupelis = food[:5] + food[3:5]*2 + food[-5:-3] + food[-5:]
print(tupelis)

# we can also change case in various way
yell = food.upper() # again original food is not changed!
print(yell)
titled_food = food.title()
print(titled_food)
capitalized_food = food.capitalize()
print(capitalized_food)
print(breakfast.title()) # all words capitalized
print(breakfast.capitalize())
quiet = breakfast.lower()
print(quiet)

dirty_city = "  \t  Rīga \t \t \n  "
print(dirty_city)
# we can clean with strip
clean_city = dirty_city.strip()
print(clean_city)
# there is also rstrip and lstrip methods if you need just one side cleaned






