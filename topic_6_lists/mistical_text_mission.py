

def mistiska_izvelne():
    print("Mistiskās izvēlnes iespējas")
    print("(1) Saskaitīt vārdus pergamentā.")
    print("(2) Atrast garāko vārdu.")
    print("(3) Parādīt unikālos vārdus alfabēta secībā.")
    print("(4) Saskaitīt konkrēta vārda parādīšanās reižu skaitu (bez reģistra jutības).")
    print('(5) Aktivizēt "Iziešanas burvestību" (iziet no programmas).')

def word_count(sentence):
    countofwords = len(sentence.split())
    print("Vārdu skaits pergamentā:", countofwords)

def find_longest_word(words: list[str]) -> str:
    # words=sentence.split()
    longest_word = max(words, key=len) # key=len means check by length of each word not lexicographically
    # print(f"The longest word is '{longest_word}' with a length of {len(longest_word)} characters.")
    return longest_word

def print_longest_word(word):
    print(f"The longest word is '{word}' with a length of {len(word)} characters.")

def find_and_print_longest_word(words):
    longest_word = find_longest_word(words)
    print_longest_word(longest_word)

def unique_words(sentence):
    words=sentence.split()
    unikalie_vardi=set(words)
    sakartots=sorted(unikalie_vardi)
    print(sakartots)

def iziesana():
    print("Jūs izvēlējāties pamest spēli!")
    print("Paldies par dalību!")

def skaitit_vardu(sentence):
    key = input("Ievadiet vārdu, kura parādīšanās reizes vēlaties uzzināt: ")
    words = sentence.lower().split() # tā sauktā normalizācija
    count = words.count(key.lower())
    print(f"Vārds '{key}' parādās {count} reizes.")

def main():
    recepte = input("Ievadiet savu mistiskā pergamenta recepti: ")
    # we could save words already here and pass them to functions
    words = recepte.split() # this is a list of words
    skaitlis=None
    i=0
    MAX_TRIES=15

    while i<MAX_TRIES:
        mistiska_izvelne()
        try:
            skaitlis = int(input("Izvēlieties mistisko iespēju: "))
            # šeit ir garantija, ka skaitlis ir vesels
        except ValueError:
            print("Ievadiet skaitli no 1 līdz 5")
            continue

        if skaitlis == 1:
            word_count(recepte)
            i+=1       
        elif skaitlis == 2:
            find_and_print_longest_word(words)
            i+=1
        elif skaitlis == 3:
            unique_words(recepte)
            i+=1 
        elif skaitlis == 4:
            skaitit_vardu(recepte)
            i+=1 
        elif skaitlis == 5:
            iziesana()
            break
        else:
            print("nepareiza izvēlne, atkārtojiet izvēli")   
            i+=1

# main guard - we will talk about this later when importing
if __name__ == "__main__": # means if this script is run directly
    main()