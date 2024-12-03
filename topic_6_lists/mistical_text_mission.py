recepte = input("Ievadiet savu mistiskā pergamenta recepti: ")

def mistiska_izvelne():
    print("Mistiskās izvēlnes iespējas")
    print("(1) Saskaitīt vārdus pergamentā.")
    print("(2) Atrast garāko vārdu.")
    print("(3) Parādīt unikālos vārdus alfabēta secībā.")
    print("(4) Saskaitīt konkrēta vārda parādīšanās reižu skaitu (bez reģistra jutības).")
    print('(5) Aktivizēt "Iziešanas burvestību" (iziet no programmas).')

def word_count():
    countofwords = len(recepte.split())
    print("Vārdu skaits pergamentā:", countofwords)

def find_longest_word():
    words=recepte.split()
    longest_word = max(words, key=len)
    print(f"The longest word is '{longest_word}' with a length of {len(longest_word)} characters.")

def unique_words():
    words=recepte.split()
    unikalie_vardi=set(words)
    sakartots=sorted(unikalie_vardi)
    print(sakartots)

def iziesana():
    print("Jūs izvēlējāties pamest spēli!")
    print("Paldies par dalību!")

def skaitit_vardu():
    key = input("Ievadiet vārdu, kura parādīšanās reizes vēlaties uzzināt: ")
    words = recepte.lower().split() # tā sauktā normalizācija
    count = words.count(key.lower())
    print(f"Vārds '{key}' parādās {count} reizes.")

mistiska_izvelne()

skaitlis=None
i=0
n=15
while i<n:
    try:
        skaitlis = int(input("Izvēlieties mistisko iespēju: "))
        # šeit ir garantija, ka skaitlis ir vesels
    except ValueError:
        print("Ievadiet skaitli no 1 līdz 5")
        continue

    if skaitlis == 1:
        word_count()
        i+=1       
    elif skaitlis == 2:
        find_longest_word()
        i+=1
    elif skaitlis == 3:
        unique_words()
        i+=1 
    elif skaitlis == 4:

        i+=1 
    elif skaitlis == 5:
        iziesana()
        break
    else:
        print("nepareiza izvēlne, atkārtojiet izvēli")   
        i+=1