# let's make a simple guessing name
secret_number = 42

guess = int(input("Try to guess my number, please enter an integer"))

# here we have 3 roads/choices - only one will be taken
if guess > secret_number:
    print("You guessed too high")
    print("Next time something lower")
elif guess < secret_number:
    print("You are too modest, next time try higher")
else: # here by exclusion only guess == secret_number remains
    print("Awesome guess! You guessed correctly", guess == secret_number)

# roads go back together
# here we could print something each time
print("You guess", guess, "correct was", secret_number)