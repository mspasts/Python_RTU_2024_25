start = 1
finish = 100

i = start
fizz = 5
buzz = 7
end_symbol = "," # so default is , for end symbol in this assignment
while i <= finish:

    # let's add and extra check to see if we have reached the last item
    if i == finish:
        end_symbol = "\n" # could also use "" if we do not want newline
    # i could have put else:
    # end_symbol = "," but instead I made it default
    
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz", end = end_symbol)
    elif i % buzz == 0:
        print("Buzz", end = end_symbol)
    elif i % fizz == 0:
        print("Fizz", end = end_symbol )
    else:
        print(i, end = end_symbol)
    i += 1