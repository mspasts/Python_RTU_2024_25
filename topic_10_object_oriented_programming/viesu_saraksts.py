import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Piemēram, viesu saraksts un ēdienu opcijas
guest_list = {}
meal_options = ["Vegetarian", "Non-Vegetarian", "Vegan", "Gluten-Free"]

# Autocomplete funkcionalitātes ieviešana
meal_completer = WordCompleter(meal_options, ignore_case=True)

def add_guest(guest_list, name, meal):
    if name not in guest_list:
        guest_list[name] = meal
        print(f"{name} tika pievienots ar '{meal}' preferenci.")
    else:
        print(f"{name} jau ir sarakstā.")

def remove_guest(guest_list, name):
    if name in guest_list:
        del guest_list[name]
        print(f"{name} tika noņemts no saraksta.")
    else:
        print(f"{name} nav atrasts sarakstā.")

def view_guests(guest_list):
    if guest_list:
        for name, meal in guest_list.items():
            print(f"{name} - {meal}")
    else:
        print("Nav pievienotu viesu.")

def count_meals(guest_list):
    meal_count = {"Vegetarian": 0, "Non-Vegetarian": 0, "Vegan": 0, "Gluten-Free": 0}
    for meal in guest_list.values():
        if meal in meal_count:
            meal_count[meal] += 1
    for meal, count in meal_count.items():
        print(f"{meal}: {count} viesi")

def is_guest_present(guest_list, name):
    if name in guest_list:
        print(f"{name} ir sarakstā.")
    else:
        print(f"{name} nav sarakstā.")

def save_guests_to_file(guest_list):
    with open("guests_list.txt", "w", encoding="utf-8") as file:
        for name, meal in guest_list.items():
            file.write(f"{name} - {meal}\n")
    print("Viesu saraksts ir saglabāts failā 'guests_list.txt'.")

def main():
    while True:
        print("\nSveicināti pasākumu organizatora programmā!")
        print("1. Pievienot viesi")
        print("2. Noņemt viesi")
        print("3. Apskatīt viesu sarakstu")
        print("4. Apskatīt maltīšu skaitu")
        print("5. Pārbaudīt viesa klātbūtni")
        print("6. Saglabāt viesu sarakstu")
        print("7. Iziet")

        choice = input("\nIzvēlieties opciju: ")

        if choice == "1":
            name = input("Ievadiet viesa vārdu: ")
            meal = prompt("Izvēlieties maltīti: ", completer=meal_completer)
            add_guest(guest_list, name, meal)
        elif choice == "2":
            name = input("Ievadiet viesa vārdu, kuru vēlaties noņemt: ")
            remove_guest(guest_list, name)
        elif choice == "3":
            view_guests(guest_list)
        elif choice == "4":
            count_meals(guest_list)
        elif choice == "5":
            name = input("Ievadiet viesa vārdu, kuru vēlaties pārbaudīt: ")
            is_guest_present(guest_list, name)
        elif choice == "6":
            save_choice = input("Vai vēlaties saglabāt viesu sarakstu (jā/nē)? ").lower()
            if save_choice == "jā":
                save_guests_to_file(guest_list)
        elif choice == "7":
            print("Paldies, ka izmantojāt programmu!")
            break
        else:
            print("Nepareiza izvēle, mēģiniet vēlreiz.")

if __name__ == "__main__":
    main()
