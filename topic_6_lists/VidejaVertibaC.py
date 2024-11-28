# Iniciējam mainīgos
total = 0
count = 0
top3 = []
bottom3 = []
all_numbers = []

print("Ievadiet skaitļus. Lai izietu, ievadiet 'q'.")

while True:
    user_input = input("Ievadiet skaitli: ")

    # if user_input.lower() == 'q':  # Iziet no programmas
    # let's be more lenient to the user and let them quit with Quit or q or Q or quitter etc
    if user_input.lower().startswith('q'):  # Iziet no programmas
        print("Programma apturēta.")
        break
    try:
        number = float(user_input)  # Pārveido ievadi uz skaitli
        total += number
        count += 1

        all_numbers.append(number)  # Pievienojam skaitli visu skaitļu sarakstam

        # TOP3 uzturēšana
        top3.append(number)  # Pievienojam jauno skaitli
        top3 = sorted(top3, reverse=True)[:3]  # Sakārtojam un saglabājam tikai 3 lielākos

        # BOTTOM3 uzturēšana
        bottom3.append(number)  # Pievienojam jauno skaitli
        bottom3 = sorted(bottom3)[:3]  # Sakārtojam un saglabājam tikai 3 mazākos

        # Aprēķina vidējo
        average = total / count # works without list
        # if list has ALL numbers
        # we can use sum function
        # len always returns the number of elements in the list
        also_average = sum(all_numbers) / len(all_numbers)

        # Izvade
        print(f"Vidējā vērtība: {average:.2f}")
        print(f"Vidējā vērtība (arī ar summu): {also_average:.2f}")
        print(f"TOP 3: {top3}")
        # also top 3 with sorted
        print(f"TOP 3 (sorted): {sorted(all_numbers, reverse=True)[:3]}")
        print(f"BOTTOM 3: {bottom3}")
        # also bottom 3 with sorted
        print(f"BOTTOM 3 (sorted): {sorted(all_numbers)[:3]}")
    except ValueError:
        print("Lūdzu ievadiet derīgu skaitli vai 'q' iziešanai.")

# Izvada visus ievadītos skaitļus
print(f"Visi ievadītie skaitļi: {all_numbers}")
