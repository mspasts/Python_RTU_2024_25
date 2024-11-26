text_input = input("Please enter an integer: ")
try:
    my_int = int(text_input) # it is possible we get an exception here
    print("This means integer conversion was great success!!")
    # safe to proceed with int stuff
    doubled = my_int * 2
    print(my_int, "doubled", doubled)
    zero_div = my_int / 0
except ValueError as error: # instead of error could be e or any other variable
    print("Error message", error)
    print("Sorry you entered someting that is not convertible to integer")
    print("You entered", text_input)
    # we could settle for some default or do something
except ZeroDivisionError as e: # i can catch multiple errors in same block
    print("You divided by zero didn't you?", e)
except: #catches all other errors, but generally we do not want to catch general errors
    print("Aliens landed or other error")
# doubled = my_int * 2
# print(my_int, "doubled", doubled)

# Takeaway: need to know the specific Error message to catch
# Full list here: https://docs.python.org/3/library/exceptions.html
# but ValueError is most common to  handle