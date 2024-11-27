#kartupelu lauks
MAX_ERRORS = 7
# TODO check if guess was already done
# we would need to store the guesses in a string(or something else)
secret_word = input("Pirmais spēlētājs ievadi jebkādu vārdu ")
 
corrected_word = ""
for char in secret_word:
    if char == " ":
        corrected_word += " "
    else:
        corrected_word += "*"
 
print("Mināmais teksts", corrected_word)

bad_guesses = 0
total_guesses = 0

while "*" in corrected_word:
    guess = input("Otrais spēlētājs vari sākt minēt ")
    total_guesses += 1
    # TODO add more instruction and check for length
    is_guess_good = False
    guessed_text = ""
    # there is a pythonic way to write this with zip
    for i in range(len(secret_word)):
        if secret_word[i].lower() == guess.lower():
            guessed_text += secret_word[i]
            is_guess_good = True # 2 or 3 or 100 times is fine
        else: # mismatch we keep the previous data
            # could be guessed letter or space or *
            guessed_text += corrected_word[i]
    corrected_word = guessed_text
    print("Atjauninātais teksts:", guessed_text)
    if not is_guess_good: # we did not get a good guess this round
        bad_guesses += 1 # bad_guesses = bad_guesses + 1
        if bad_guesses >= MAX_ERRORS:
            print("Sorry your luck run out!")
            print("You guessed badly ", bad_guesses, "times")
            break
if bad_guesses < MAX_ERRORS:
    print("Apsveicu Winner Winner Chicken Dinner")
    print("You guessed badly", bad_guesses, "times")
    print("You total guesses", total_guesses, "times")
else:
    print("Correct answer was", secret_word)