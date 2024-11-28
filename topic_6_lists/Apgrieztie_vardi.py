print("Lai izietu no programmas ievadiet 'q' ")

while True:
    try:
        lietotaja_ievade = input("Lūdzu ievadiet jebkādu teikumu: ")
        if lietotaja_ievade.lower() == 'q':
            print("Visu gaišu")
            break

        ievade = lietotaja_ievade.split()
        apgriezti_vardi = []
        if ievade:
            pirmais_vards = ievade[0][::-1].capitalize()
            apgriezti_vardi.append(pirmais_vards)

        for vards in ievade[1:]:
            apgriezti_vardi.append(vards[::-1])
        
        apgriezts_teikums = ' '.join(apgriezti_vardi)
        print(apgriezts_teikums)
    
    except ValueError:
        print("Nepareiza ievade")