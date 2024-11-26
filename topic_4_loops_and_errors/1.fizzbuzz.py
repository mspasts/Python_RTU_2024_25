# for loops are for iterating/looping through definite number of items
# in iterable (something we can loop through)

# compared to while loop
# we can declare our variable inside loop
print("Let's play fizzbuzz!")

end = ","
for i in range(1, 100+1):
    if i == 100:
        end = "\n" # newline
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz", end=end)
    elif i % 5 == 0:
        print("Fizz", end=end)
    elif i % 7 == 0:
        print("Buzz", end=end)
    else:
        print(i, end=end)