
def pievienot_viesi(viesu_saraksts, vards, ediens, ediens_menu):
    if vards in viesu_saraksts:
        print(f"{vards} jau ir viesu sarakstā.")
        return
    if ediens not in ediens_menu:
        print(f"Tāds ēdiens nav pieejams, pieejamie ēdieni ir: {', '.join(ediens_menu)}")
        return
    viesu_saraksts[vards] = ediens
    print(f"{vards} tika pievienots ar izvēlēto ēdienu - \"{ediens}\".")

def dzest_viesi(viesu_saraksts, vards):
    if vards in viesu_saraksts:
        del viesu_saraksts[vards]
        print(f"{vards} tika dzēsts no viesu saraksta.")
    else:
        print(f"{vards} nav viesu sarakstā.")

def apskatit_viesus(viesu_saraksts):
    if viesu_saraksts:
        print("viesu saraksts:")
        for vards, ediens in viesu_saraksts.items():
            print(f"{vards}: {ediens}")
    else:
        print("Viesu saraksts ir tukšs.")

def edienu_skaits(viesu_saraksts, ediens_menu):
    # create a default dictionary with 0 values for each meal
    ediens_skaitss = {ediens: 0 for ediens in ediens_menu}
    for ediens in viesu_saraksts.values():
        if ediens in ediens_skaitss:
            ediens_skaitss[ediens] += 1
    print("Ēdienu skaits:")
    for ediens in ediens_menu:
        print(f"{ediens}: {ediens_skaitss[ediens]}")

def vai_viesis_pastav(viesu_saraksts, vards):
    if vards in viesu_saraksts:
        print(f"{vards} ir viesu sarakstā.")
    else:
        print(f"{vards} nav viesu sarakstā.")

# so we have some global state here - truth about our world - guests and their meals
viesu_saraksts = {} 
ediens_menu = ["🥑vegānu", "🍖grills", "🧀sieru plates", "🍘bez glutēna"] 

while True:
    print("\nEsi sveicināts restorāna pārvaldības programmā!")
    print("1. Pievienot viesi")
    print("2. Izslēgt viesi no saraksta")
    print("3. Pārbaudīt viesu sarakstu")
    print("4. Pārbaudīt ēdienu sarakstu")
    print("5. Pārbaudīt vai viesis ir sarakstā")
    print("6. Iziet")
    izvele = input("Izvēlieties jums vēlamo opciju: ")

    if izvele == "1":

        vards = input("Ievadiet viesa vārdu: ")
        print(f"Pieejamie ēdieni: {', '.join(ediens_menu)}")
        ediens = input("Izvēlieties ēdienu: ")
        pievienot_viesi(viesu_saraksts, vards, ediens, ediens_menu)
    elif izvele == "2":

        vards = input("Ievadiet viesa vārdu, ko izslēgt no saraksta: ")
        dzest_viesi(viesu_saraksts, vards)
    elif izvele == "3":

        apskatit_viesus(viesu_saraksts)
    elif izvele == "4":

        edienu_skaits(viesu_saraksts, ediens_menu)
    elif izvele == "5":

        vards = input("Kādu viesi jūs meklējat: ")
        vai_viesis_pastav(viesu_saraksts, vards)
    elif izvele == "6":

        print("Lai jauka diena!")
        break
    else:
        print("Nepareiza ievade, lūdzu mēģiniet vēlreiz.")
