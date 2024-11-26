# let's make a guessing game
secret = 42 # could get from random
# or could get from second user
guess = int(input("Please enter an integer to guess"))
attempts = 0
MAX_ATTEMPTS = 7


# while True:
while attempts < MAX_ATTEMPTS:
    if secret == guess:
        print("Congratulations! you win")
        print("You guess correctly answer was", secret) # guess too
        break # we leave current inner while loop
    elif guess > secret:
        print("you guessed too high please try again")
    else: # or elif guess < secret
        print("You guessed too low, try again")
    attempts += 1 # to keep track of attempts
    guess = int(input("Please enter an integer to guess"))

if attempts < MAX_ATTEMPTS:
    print(f"Cool you won in {attempts} tries")
else:
    print(f"Sorry you exceeded maximum attempts you made {attempts} tries")
print("All done game over!")