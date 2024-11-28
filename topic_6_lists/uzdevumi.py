teikums = input("Ievadiet teikumu: ") #iegūstam teikumu
vardi = teikums.split() #sadalīšana
jaucam_vardus = [vardi[::-1] for vardi in vardi] #taisam jucekli
jauc_teikumu = " ".join(jaucam_vardus)#teikuma sakārtošana
print(f"Vai pats saprati, ko esi uzrakstījis: {jauc_teikumu}")

kopa = 0  
skaits = 0 
print("Ievadi skaitli lai iegūtu vidējo summu, vai ja vēlies iziet 'q'.")
while True:
    liet_ievad = input("ievadi skaitli: ")
    if user_input.lower() == 'q':
        print("Beigas.")
        break
    try:
        skaitlis = float(liet_ievad)
        kopa += skaitlis            
        skaits += 1                 
        vid = kopa / skaits
        print(f"Tu ievadīji {count} skaitļus: (vidējais skaitlis ir: {average:.2f})")
    except ValueError:
        print("Ievadiet derīgu skaitli vai 'q' ja vēlies beigt.")