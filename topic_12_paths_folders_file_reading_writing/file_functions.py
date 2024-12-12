import os

# Definējam 3 funkcijas clean_file, clean_file_many un clean_folder_many_texts

# Definējam funkciju, kas attīrīs vienu failu, saglabājot tās rindas, kas atbilst good_text un bad_text 
def clean_file(src_file, dest_file, good_text="", bad_text=""):

    #Ar šo mēs atveram failu un nolasām
    with open(src_file, 'r', encoding='utf-8', errors='replace') as f_in: #readlines() lasa visas faila rindas kā sarakstu
        lines = f_in.readlines()
    # again src file is closed here

    filtered_lines = []
    for line in lines:
        line_stripped = line.strip('\n')
        # Definējam nosacījumus kas būs atkarīgi no good_text un bad_text
        if good_text == "" and bad_text == "":
            # ja abi nosacījumi ir tukši - saglabājam visas rindiņas
            filtered_lines.append(line_stripped)
        elif good_text == "" and bad_text != "":
            # Ja nav good_text, bet ir bad_text saglabājam tikai tos kas nav bad_text
            if bad_text not in line_stripped:
                filtered_lines.append(line_stripped)
        elif good_text != "" and bad_text == "":
            # Ja ir good_text, bet nav bad_text saglabājam tikai tos kas ir good_text
            if good_text in line_stripped:
                filtered_lines.append(line_stripped)
        else:
            # Ja ir gan tur gan tur tad saglabājam tikai tos kas ir good_text bet nav bad_text
            if good_text in line_stripped and bad_text not in line_stripped:
                filtered_lines.append(line_stripped)

    #Saglabājam rezultātus jaunā failā
    with open(dest_file, 'w', encoding='utf-8') as f_out:
        for fl in filtered_lines:
            f_out.write(fl + '\n')

    print(f"Fails {src_file} apstrādāts, rezultāts saglabāts failā {dest_file}")

# Definējam clean_file_many funkciju, kas ir ļoti līdzīga clean_file, taču atbalsta vairākus good un bad text'us

def clean_file_many(src_file, dest_file, good_texts=(), bad_texts=()):

    #Uzsākam faila nolasīšanu
    with open(src_file, 'r', encoding='utf-8', errors='replace') as f_in:
        lines = f_in.readlines()

    filtered_lines = []
    for line in lines:
        line_stripped = line.strip('\n')

        if not good_texts and not bad_texts:
            filtered_lines.append(line_stripped)
            continue

        #Ar any() pārbaudām saturēšanu, ar good_condition pārbaudām rindu vai uz good_text elementiem
        if good_texts:
            good_condition = any(g in line_stripped for g in good_texts)
            # if we did not know about any we could do the same with loop
            # good_condition = False
            # for g in good_texts:
            #     if g in line_stripped:
            #         good_condition = True
        else:
            good_condition = True 

        #Respektīvi tas pats, kas iepriekš, tikai šeit mēs pārbaudām rindiņas uz bad_text elementiem
        if bad_texts:
            bad_condition = any(b in line_stripped for b in bad_texts)
        else:
            bad_condition = False

        if good_condition and not bad_condition:
            filtered_lines.append(line_stripped)

    with open(dest_file, 'w', encoding='utf-8') as f_out:
        for fl in filtered_lines:
            f_out.write(fl + '\n')

    print(f"Fails {src_file} apstrādāts, rezultāts saglabāts failā {dest_file}")

# Definējam _clean_folder_many_texts funkciju, kas izmanto visus failus mapē ar paplašinājumu *.txt

def clean_folder_many_texts(src_folder, 
                            dest_folder, 
                            src_postfix=".txt", 
                            dest_postfix="_cleaned.txt", 
                            good_texts=(), 
                            bad_texts=()):

    #Pārbaudām good un bad texts uz satura esamību
    if not good_texts and not bad_texts:
        raise ValueError("good_text un bad_text nesatur datus")

    #Pārbaudām, vai src_folder pastāv
    if not os.path.exists(src_folder):
        print(f"Source mape {src_folder} neeksistē.")
        return

    #Ja dest_folder nepastāv ar šo komandu veicam tās izveidi projekta mapē
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder) #makedirs will make as many folders as needed my_folder/my_subfolder/etc
    # with pathlib.Path(dest_folder).mkdir(parents=True, exist_ok=True) # alternative way to create folder

    #Pārbaudām visus failus ar *.txt paplašinājumu
    all_files = [f for f in os.listdir(src_folder) if f.endswith(src_postfix)]
    if not all_files:
        print(f"Mape {src_folder} nesatur failus ar paplašinājumu {src_postfix}.")
        return

    #Ar šo katrs atrastais fails ar *.txt tiks apstrādāts
    processed_files = []
    for file_name in all_files:
        src_file_path = os.path.join(src_folder, file_name)
        dest_file_name = file_name.replace(src_postfix, dest_postfix)
        dest_file_path = os.path.join(dest_folder, dest_file_name)
        # with pathlib we could do the same with Path
        # src_file_path = pathlib.Path(src_folder) / file_name
        # dest_file_path = pathlib.Path(dest_folder) / dest_file_name

        #Izmantojam clean_file_many, lai attīrītu failu, pēc kā katram apstrādātajam failam pievienojam prefiksu ka fails ir apstrādāts
        clean_file_many(src_file_path, dest_file_path, good_texts=good_texts, bad_texts=bad_texts)
        processed_files.append((src_file_path, dest_file_path))

    # rezultāts
    print(f"Faili atrastie mapē: {src_folder} apstrādāti")
    print(f"Attīrītie faili saglabāti: {dest_folder} mapē")
    for src, dst in processed_files:
        print(f"{src} -> {dst}")

# let's use clean_folder_many_texts



