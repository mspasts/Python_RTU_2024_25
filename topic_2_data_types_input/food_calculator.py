# let's make a simple interactive food calculator
print("Ši programma aprēķina Jūsu mīļākā ediena cenu")
# first let's get the name of you - that is the person
# so that will be our first variable
# name = "Valdis" # this would be hard coded value
# instead let's ask for the name
name = input("What is your name, friend? ")
# could use empty name = input() # no text prompt then
# everything typed before pressing enter will be saved into name variable
print(f"Now, that is a nice name - {name}, I rather like it :)")

# again input always returns a string
# our variables have data types
# you can get the type with type(variable) function
# print("Type of name variable is", type(name))
# typically we do not need to use type except when debugging

# just like print, I can use f-strings inside input
food = input(f"What is your favorite food, {name}?")
print(f"Awesome, I love {food} myself")

# now let's get the price
print(f"So {name}, what price is for 1kg of {food} in your corner store?")
price = input("->") # this will be in new line
print(f"Oh, {price} for 1kg of {food}, that's quite a bit, isn't it?")
price_2kg = price * 2
print(f"So 2kg of {food} would be {price_2kg}, would it?") # think..
# since price is still string we got a string doubled which is not what we want

# we need to cast price to float - number with decimal point
price = float(price) # float attempts to convert other data type to float
price_3kg = price * 3
print(f"Now 3kg of {food} should really be {price_3kg}")
# let's ask for quantity
quantity = input(f"How many kg of {food} do you want to buy {name}?")
# quantity is again guaranteed to be a string
# let's assume that user always enters a whole number of kg here
# in real life that might not be so
quantity = int(quantity) # again i could have used new variable on the left side

# we are almost ready to calculate the food price
total = price * quantity
print(f"Alrighty! So {quantity}kg of {food} would cost {total} in your nearest store.")

# we might want to round the result - to avoid any float shenanigans
total_rounded = round(total, 2) # so 2 digits after comma
print("Total rounded is", total_rounded)

# we learned about 3 data types str, int, float - so called primitive types
# Python has a few more primitive types - soon on those




