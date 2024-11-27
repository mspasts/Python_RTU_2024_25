# so far we know primitive data types
# such as int, float, str, bool
# what happens if we have many similar data types?
# if we do not know any better we could try this...
a1 = 1
a2 = 2
a3 = 3
a4 = 5
a5 = 8
a6 = 13
# this is of course Fibonacci sequence
# what if we have 100, or 1000 numbers?

# instead Python offers us a list data type - this is similar to arrays in other languages
# not to be confused with linked list - that is a different data structure

# Python saraksti ir saraksts ar elementiem, kas ir sakartoti un numurēti, sākot ar 0

# main idea behind lists is that we can store multiple values in a single variable
# what can we do with lists?
# 1. create a list
# 2. access elements of a list
# 3. change elements of a list - mutable
# 4. add elements to a list - dynamic size / resizable
# 5. remove elements from a list - dynamic size / resizable
# 6. iterate through a list
# 7. sort a list
# 8. search for elements in a list
# 9. some other operations

# we will see that some things are quite similar to string operations

# first let's create a list - for now empty
# we can create a list by using square brackets []
my_list = [] # so this is an empty list
print(my_list) # []

# how many elements are in the list?
print(f"Number of elements in the list: {len(my_list)}") # 0 # remember len also worked on strings