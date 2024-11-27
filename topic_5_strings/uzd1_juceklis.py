# Lietotājs ievada vārdu.
# Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu teksu pamatīgs juceklis vai ne pirmais lietotāja burts?
# Valdis -> Sidlav, pamatigs juceklis vai ne V?
 
name=input("Kāds ir tavs vārds?")
name_reverse=name[::-1]
capitalized_n = name_reverse.capitalize()
print(capitalized_n, ",pamatīgs juceklis vai ne pirmais", name[0])

rev_name = name[::-1].capitalize()
 
add_text = f"pamatīgs juceklis vai ne {name[0].upper()}?"
 
print(f"{rev_name}, {add_text}")