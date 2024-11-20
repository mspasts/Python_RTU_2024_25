# we can do some operations with booleans
# in programming this is all the math you need :)
# we need only 3 basic operations, negation, conjuction and disjunction
# https://en.wikipedia.org/wiki/Boolean_algebra
# simplest is negation
# in Python we use English not (unlike most languages which use !)
print("not True ->", not True)
print("not False ->", not False)

is_raining = True
reverse_of_is_raining = not is_raining
print("reverse of is_raining", reverse_of_is_raining)
print("is it raining? ", is_raining)
# we can reassign to same variable so like a button on /off
is_raining = not is_raining # so this works as a toggle
print("is it raining? ", is_raining)
is_raining = not is_raining # so this works as a toggle
print("is it raining? ", is_raining)
is_raining = not is_raining # so this works as a toggle
print("is it raining? ", is_raining)

print("*"*40)
# next we have conjuction
# BOTH sides have to be True for the operation to be True
print("True and True ? ", True and True) # True
print("True and False ? ", True and False) # False
print("False and True ? ", False and True) # False
print("False and False ? ", False and False) # False

print("*"*40)
# typically we would use some variables in logical operations

# finally we have disjunction as basic logical operation
# At least one side should be True for operation to be True
print("True or True ? ", True or True) # True
print("True or False ? ", True or False) # True
print("False or True ? ", False or True) # True
print("False or False ? ", False or False) # False
