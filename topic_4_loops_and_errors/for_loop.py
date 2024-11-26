# so for loops are for looping through SOME collection of items
# Python has many different iterable collections
# we can even make our own

# basic for loop using range to print some numbers
for i in range(5): # range is iterable that gives you numbers on demand
    print(f"I am number {i}")
    
print("Outside At end the number is", i)

j = 0
while j < 5:
    print(f"j is now {j}")
    j += 1
print("outside loop j is", j)

# we can loop through strings with for loop
name = "Valdis"
for char in name: # could use c, or it, or item, element etc
    print("Current char is", char)
    
    