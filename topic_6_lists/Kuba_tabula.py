print("Lai izietu no programmas ievadi 'q'")
while True:
    try:
        sakuma_skaitlis = input("Lūdzu ievadi sākumskaitli: ")
        if sakuma_skaitlis.lower() == 'q':
            print("Paldies ka izmantojāt 'Kubu Tabulu'")
            break

        beigu_skaitlis = input("Lūdzu ievadi beigu skaitli: ")
        if beigu_skaitlis.lower() == 'q':
             print("Paldies ka izmantojāt 'Kubu Tabulu'")
             break
    
        sakuma_skaitlis = int(sakuma_skaitlis)
        beigu_skaitlis = int(beigu_skaitlis)
        # here we know that we have integers for both sakuma_skaitlis and beigu_skaitlis
        kubi = []
        for i in range(sakuma_skaitlis, beigu_skaitlis + 1):
            kubs = i ** 3
            kubi.append(kubs)
            print(f" {i} kubā: {kubs}")

        print(f"Visi kubi: {kubi}")
    except ValueError:
        print("Nepareiza ievade lūdzu ievadiet veselu skaitli vai 'q' iziešanai.")