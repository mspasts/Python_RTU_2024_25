from pathlib import Path 
 
all_files = list(Path.cwd().iterdir())
all_txt_files = [file for file in all_files if file.suffix == ".txt"]
 
# 1.a 
def file_line_len(fpath):
    try:
        counter = 0
        with open(fpath, 'r', encoding='utf-8') as file:
            # lines = file.readlines() # this reads all lines into a list of strings into memory
            # other approach would be to iterate over the file object
            # then we can count the lines in a very large file without loading all lines into memory
            for _ in file: # note I could use _ instead of line since I don't use it
                counter += 1
        # when file is closed we return the counter
        return counter
        # return len(lines)
    except FileNotFoundError:
        print(f"ERROR -  Nepareiza adrese '{fpath}' !")
        return -1
# i will add relative path to the file 
# since we are one level up from topic_12_paths_folders_file_reading_writing folder
# result = file_line_len("topic_12_paths_folders_file_reading_writing/veidenbaums.txt")
# once we have changed our terminal directory to topic_12_paths_folders_file_reading_writing
# then we have the following
result = file_line_len("veidenbaums.txt")
print(result)

# 1.b.
def get_poem_lines(fpath):
 
    poem_lines = []
 
    with open(fpath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
 
            if len(line) == 0:
                continue
            # another rule is to check that *** are present in line , this means title, and not needed
            if "***" in line:
                continue
            # note we could have combined the two rules into one
 
            poem_lines.append(line)
 
    return poem_lines

# 1.c
def save_lines(destpath, lines, endline="\n"): # this way if there is no need to add endline, it will be added by default
    with open(destpath, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + endline)
 
dzeja = get_poem_lines("veidenbaums.txt")
save_lines("mans_veidenbaums.txt", dzeja)

import string
bad_chars = string.punctuation

# we will create a function that takes file src and file dst and punct arguments
# and saves the cleaned file
def clean_punkts(src_file, dest_file, bad_chars=bad_chars):
    with open(src_file, 'r', encoding='utf-8') as file:
        text = file.read()

    for punkt in bad_chars:
        text = text.replace(punkt, "")
    # alternative would be to use translate method which uses dictionary
    # more on translate method here: https://www.w3schools.com/python/ref_string_maketrans.asp
 
    with open(dest_file, 'w', encoding='utf-8') as file:
        file.write(text)

# so let's give mans_veidenbaums.txt as src and mans_veidenbaums_cleaned.txt as dest
clean_punkts("mans_veidenbaums.txt", "mans_veidenbaums_cleaned.txt") #note I use default bad_chars

# now let's use custom bad chars 
custom_bad_chars = string.punctuation + "…" # could add other chars

# now let's try again
clean_punkts("mans_veidenbaums.txt", "mans_veidenbaums_cleaned_custom.txt", custom_bad_chars) #note I use custom bad_chars



# leaving 1.f as exercise for the reader

# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
# ieteikums izmantot Counter moduli !
# uzskatīsim, ka vārdi tiek atdalīti vai nu ar whitespace vai newline (vecais labais split noderēs)

# populārāku vārdu sarakstu ar lietojuma biežumu saglabājam destpath