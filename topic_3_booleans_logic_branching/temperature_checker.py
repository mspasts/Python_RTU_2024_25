# let's use booleans to have computer make choice / branch
# let's ask user for temperature outside
# we can cast immediately 
temperature = float(input("What is temperature outside?"))
# instead of input it could be reading some sensor or reading data from internet
# t would be okay variable name here
print(f"So outside is {temperature}")

# let's have computer offer us suggestion on what to wear
# let's say if temperature is over 30 degrees Celsius
# then tell user to drink lots of water

# line 15 will only run if temperature > 30 gives us True value
if temperature > 30: # in Python : is usually followed by indentation
    print("This is quite hot! Drink lots of water")
    # we are still inside the if block
    
# we are in main block
print("Let's check temperature again...")

if temperature < 0:
    print("Brrrrr!, Take skates to work!")
    # this is completely different block

# print("Ohh that is nice temperature", temperature)

# sometimes we want to take ONLY one road from two choices
# if True do one, if False do something else

if temperature > 4:
    print("You probably want summer tires")
    print("Outside is", temperature)
else: # Means temperature is 4 or Less
    print("Think about getting winter tires!")
    print("Getting cold outside at", temperature)
    
# back to global block our roads go back together
print("Whew we are finished! This always runs")