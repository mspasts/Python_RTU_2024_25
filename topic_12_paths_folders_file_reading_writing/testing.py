from file_functions import clean_file, clean_file_many, clean_folder_many_texts

while True:
    print("Izvēlies, kuru funkciju testēt:")
    print("1 - Clean File")
    print("2 - Clean File Many")
    print("3 - Clean File Many Texts")

    choice = input("Izvēlieties atbilstošo vai nospiediet 'q' lai izietu: ").strip()

    if choice == "1":
        clean_file("input.txt", "output.txt", good_text="python", bad_text="error")
    elif choice == "2":
        clean_file_many("input.txt", "output.txt", good_texts=["python","test"], bad_texts=["error"])
    elif choice == "3":
        clean_folder_many_texts("src_folder", "dest_folder", src_postfix=".txt", dest_postfix="_apstradatais.txt", good_texts=["apple","car"], bad_texts=["error"])
    elif choice.lower() == "q":
        print("Testēšanas vide tiek aizvērta.")
        break
    else:
        print("Tāda izvēle nepastāv.")
    print()