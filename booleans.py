# let's learn another data type - boolean
# in a way the simplest yes/no, white/black,on/off, True/False
# so boolean has only two values True and False
is_snowing = False # good idea to use is_ for variables that are boolean
is_cold = True
#flag is often used as a variable for booleans but that is not descriptive enough
print("Is snowing?", is_snowing)
print("Is cold?", is_cold)

print("So type of is_snowing is", type(is_snowing))

# so how do we get these Booleans
# we can use comparison operators
print("5 > 3 ?", 5 > 3)
print("2 > 3 ?", 2 > 3)

# i can save results in a variable of comparison
is_math_correct = 10 < 9 + 2 # so + will go first then comparison < then =
print("Whew so 10 < 9 + 2?", is_math_correct)

# often we want to use variables in comparing
a = 2
b = 3
c = 4

print("b < a", b < a)

# we also have less than and equal <=
# and greater or equal >=
print("a*a <= c ?", a*a, c, a*a <= c) # should be True

print("a*b >= c ?", a*b, c, a*b >= c) # should be True

# we also have equality and inequality
print("Is a*a equal to c?", a*a == c)
print("Is a*a NOT equal to c?", a*a != c)

# we can compare strings as well
name = "Valdis"
neighbor = "Voldemārs"
print(f"{name} < {neighbor} ? {name < neighbor}")
neighbor = "Vol"
print(f"{name} < {neighbor} ? {name < neighbor}")
neighbor = "Valda"
print(f"{name} < {neighbor} ? {name < neighbor}")


