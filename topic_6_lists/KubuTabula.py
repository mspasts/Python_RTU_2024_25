#kubi
# # Lūdzam lietotājam ievadīt sākuma un beigu skaitļus
try:
    start = int(input("Ievadiet sākuma skaitli (vesels skaitlis): "))
    end = int(input("Ievadiet beigu skaitli (vesels skaitlis): "))

    if start > end:
        print("Sākuma skaitlim jābūt mazākam vai vienādam ar beigu skaitli.")
    else:
        # Izveidojam sarakstu ar visiem skaitļiem no sākuma līdz beigām
        numbers = list(range(start, end + 1))

        # Aprēķinām kubus
        cubes = [num ** 3 for num in numbers]

        # Izvadām rezultātus
        print(f"A. Jūs izvēlējāties skaitļus: {', '.join(map(str, numbers))}.")
        print(f"B. Jūsu ievadīto skaitļu kubi ir: {', '.join(map(str, cubes))}.")
except ValueError:
    print("Lūdzu ievadiet tikai veselus skaitļus.")
