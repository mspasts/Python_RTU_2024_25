# we can combine while with try to guarantee certain operations
total = 0

while True:
    try:
        raw_input = input("Please enter an integer or q to quit!")
        if raw_input == "q": # we check first for quitting symbol(s)
            # TODO make the quitting condition friendlier qQ  or Quit quit
            print("okay quitting time")
            break # we break the loop
        number = int(raw_input)
        # here we have an integer for sure
    except ValueError:
        print("Sorry that was not an integer! Please Enter again")
        continue # goes back to start of while loop
    # here too we have number as integer
    total += number # so same as total = total + number
    print("Current total is", total)
    
print("Well done we are finished", total)