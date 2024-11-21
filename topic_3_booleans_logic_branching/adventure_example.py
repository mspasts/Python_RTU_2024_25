#pirmais posms
print("Sākuma telpa")
print("Tu pamosties slēgtā telpā. Uz galda ir atslēga, un logs ir nedaudz pavērts")
print("Ko tu darīsi?")
print("1: Paņem atslēgu")
print("2: Kāp ārā pa logu")

izvele = input("Ievadi savu izvēli (1 vai 2): ") #lietotājas ievada numuru 1 vai 2

if izvele =="1":
    #pāreja uz 2 posmu
    print("\nAizslēgtās durvis")
    print("Tu pieej aizslēgtajām durvīm. Atslēga, ko paņēmi, der slēdzenei. Tu dzirdi soļus ārpusē.")
    print("Ko tu darīsi")
    print("1: Atver durvis")
    print("2: Pagaidi")
    
    izvele = input("Ievadi savu izvēli (1 vai 2): ") #lietotājas ievada numuru 1 vai 2
    
    if izvele =="1":
        #pāreja uz 3 posmu
        print("\nVirtuve")
        print("Tagad tu esi virtuvē. Ir durvis, kas ved ārā, bet signalizācija ir ieslēgta.")
        print("Ko tu darīsi")
        print("1: Atslēdz signalizāciju")
        print("2: Skrien caur durvīm")
        
        izvele = input("Ievadi savu izvēli (1 vai 2): ") #lietotājas ievada numuru 1 vai 2
        
        if izvele =="1":
            print("Tu atslēdzi signalizāciju un veiksmīgi izbēgi")
            
            if izvele =="1":
                print("\nTu domāji ka uzvarēji bet tev bēgot sapinās zābakšņores un tu pakriti")
                print("\nTev palīgā pienāk divi cilvēki un abi sniedz roku")
                print("Pirmais ir krimināla paskata vīrieties")
                print("Otrais ir policists")
                print("Kurš tev palīdzēs")
                print("1: Krimināla paskata vīrietis")
                print("2: Policists")
                
                izvele = input("Ievadi savu izvēli (1 vai 2): ") #lietotājas ievada numuru 1 vai 2
                
                if izvele =="1":
                    print("\nVīrietis izrādījās ļoti laipns biznesmenis kas vienkārši ir no 90-ajiem")
                    print("Vīrietis tev pasniedz saini ar 100 000 eur un atvadās, tu laimīgs ej svinēt")
                    print("\nSpēles beigas")
                    
                elif izvele =="2": #nepareizā atbilde pie pakrišanas
                    print("\nPolicists tevi aiztur par to ka tu blandījies svešā mājā par ko bija ziņojuši kaimiņi")
                    print("Tev piespriež 24 mēnešus sabiedrisko darbu")
                    print("\nSpēles beigas")
                else: #spēles beigas ja lietotājs ievada neatbilstošu variantu (ciparu kas nav minēts)
                    print("\nNederīga atbilde, spēles beigas")
                
        elif izvele =="2": #nepareizā atbilde virtuves posmam
            print("\nSpēles beigas")
            print("Signalizācija sāka skanēt, un tevi noķēra!")
        else: #spēles beigas ja lietotājs ievada neatbilstošu variantu (ciparu kas nav minēts)
            print("\nNederīga atbilde, spēles beigas")
                
    elif izvele == "2": #nepareizā atbilde aizslēgto durvju posmam
        print("\nTu gaidīji pārāk ilgi, un kāds tevi ieslēdza")
    else: #spēles beigas ja lietotājs ievada neatbilstošu variantu (ciparu kas nav minēts)
        print("\nNederīga atbilde, spēles beigas")
        
elif izvele =="2": #nepareizā atbilde sākuma posmam
    print("\nTu mēģināji izkāpt, bet tas ir par augstu. Tu nokriti.")
else: #spēles beigas ja lietotājs ievada neatbilstošu variantu (ciparu kas nav minēts)
    print("\nNederīga atbilde, spēles beigas")
        



   
