user_input = input("Ievadiet tekstu " )
print("Jūs ievadījāt sekojošo tekstu: ", user_input)

if "nav" in user_input and "slikts" in user_input:
    # te mēs zinam ka ir gan "nav", gan "slikts"
    nav = user_input.find("nav")
    slikts = user_input.find("slikts") 
    # vēl jāparbauda vai "nav" ir pirms "slikts"
    if nav < slikts: # mēs pārbaudām indeksu vai "nav" ir pirms "slikts"
        slikts_beigas = slikts + len("slikts")
        aizvietosana = user_input[:nav] + "ir labs" + user_input[slikts_beigas:]
        print("Tā būs pareizāk: ", aizvietosana)
    else: # nozimē ka "slikts" ir pirms "nav" un tas nav pareizi, tad nemainam neko
        print("Teksts kā es to redzu: ", user_input)
else:
    print("Piekrītu tavam domu gājienam")
    print("Teksts kā es to redzu: ", user_input)