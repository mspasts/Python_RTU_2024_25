# let's talk about paths and directories in Python

# first let's talk about concept of current working directory
# current working directory is the directory from which the script is running

# let's find out where we are

# first let's use datetime module to get current date and time
from datetime import datetime # this is how you import class from module
# datetime is a class in datetime module - so double name

import os # this is old school way of importing modules
print("Current working directory is: ", os.getcwd()) # os.cwd() returns string with the current working directory
# a more modern approach is to use pathlib module

from pathlib import Path # this is the newer recommended way of working with paths and files
print("Current working directory is: ", Path.cwd()) # Path.cwd() returns a Path object with the current working directory
# difference is that Path object is more versatile and has more methods and properties and it works 
# better across different operating systems

# I could change the directory with os.chdir() or Path.cwd().chdir() 
# let's change to topic_12_paths_folders_file_reading_writing directory using Path if I did not already do that
# os.chdir(Path.cwd() / "topic_12_paths_folders_file_reading_writing")

# let's check if we are in the right directory
print("Current working directory is: ", Path.cwd())

# let's talk about absolute and relative paths

# absolute path is the full path from the root directory to the file or directory 
# absolute path is unique for each file or directory

# let's find out what is in the current directory

all_files = list(Path.cwd().iterdir()) # Path.cwd().iterdir() returns a generator object with all files and directories in the current directory
print("All files in the current directory: ", all_files)

# let's save only file names
all_files_names = [file.name for file in all_files] # file.name returns the name of the file or directory
print("All files names in the current directory: ", all_files_names)

# how about just the stem of the file name
all_files_stems = [file.stem for file in all_files] # file.stem returns the stem of the file name
print("All files stems in the current directory: ", all_files_stems)

# i could get extension of the file
all_files_extensions = [file.suffix for file in all_files] # file.suffix returns the extension of the file
print("All files extensions in the current directory: ", all_files_extensions)

# how about direct parent directory of each file
all_files_parents = [file.parent for file in all_files] # file.parent returns the parent directory of the file
print("All files parent directories in the current directory: ", all_files_parents)

# so now I could get all txt files in the current directory using list comprehension
all_txt_files = [file for file in all_files if file.suffix == ".txt"]
print("All txt files in the current directory: ", all_txt_files)

# there is another way to get all txt files using Path.glob() method
# glob looks in current directory only
all_txt_files_glob = list(Path.cwd().glob("*.txt")) # so all files with txt extension
print("All txt files in the current directory using glob: ", all_txt_files_glob)

# we can use rglob to recursively search for files in all subdirectories
# it is similar to glob but it searches in all subdirectories
# it is also similar to how Windows search works in Explorer
all_txt_files_rglob = list(Path.cwd().rglob("*.txt")) # so all files with txt extension in all subdirectories
# in this case we do not have any subdirectories so it will be the same as glob
print("All txt files in the current directory using rglob: ", all_txt_files_rglob)

# we might want to go up one level from cwd for that we can use .. in the path

# let's go up one level when using rglob but first we use Path("../") to go up one level
all_txt_files_rglob_parent = list(Path("../").rglob("*.txt")) # so all files with txt extension in all subdirectories
print("All txt files in the parent directory using rglob: ", all_txt_files_rglob_parent)

# note something about returned Paths - they are NOT absolute paths
# they are relative paths to the current working directory

# we could get absolute paths using resolve() method
all_txt_files_rglob_parent_absolute = [file.resolve() for file in all_txt_files_rglob_parent]
print("All txt files in the parent directory using rglob with absolute paths: ", all_txt_files_rglob_parent_absolute)

# so how could I find all .txt files in D: drive Github folder and its subdirectories
root_drive_path = Path("D:/") # root of the D: drive - could take LOOOONG time
# root_drive_path = Path("D:/Github") # this is how you define a path to a drive  and first level folder this is absolute path!
root_drive_path = Path("D:/Github/Python_RTU_2024_25") # this is now absolute path to the folder and its subfolder
# let's get current time
start_time = datetime.now()
all_txt_files_drive = list(root_drive_path.rglob("*.txt")) # so all files with txt extension in all subdirectories
# this could take some time....
end_time = datetime.now()
print(f"I have found {len(all_txt_files_drive)} txt files in D: drive")
# it took how long?
print("It took: ", end_time - start_time)

# now absolute paths - D:\Github\Python_RTU_2024_25\topic_12_paths_folders_file_reading_writing\rainis.txt
# have to be careful with backslashes in Windows - they are escape characters in Python
# instead we could use raw strings - r"string" - it will not interpret escape characters
# rainis_path = Path(r"D:\Github\Python_RTU_2024_25\topic_12_paths_folders_file_reading_writing\rainis.txt")
# you could use forward slashes in Windows - they work just fine
rainis_path = Path("D:/Github/Python_RTU_2024_25/topic_12_paths_folders_file_reading_writing/rainis.txt")
# assert path exists
assert rainis_path.exists(), "Rainis file does not exist!"
print(f"Ready to read Rainis file from absolute path: {rainis_path}")

# first try will use with context manager and we will use open() function
with open(rainis_path, encoding="utf-8") as file: # open() function opens the file in read mode
    # file is a file stream object
    # rainis path could be a string or Path object
    # we uses encoding="utf-8" to specify that the file is in UTF-8 encoding, these days this is 99% of the time
    # default is read mode
    rainis_text = file.read() # file.read() reads the whole file into a string, potentially huge string
    # file is still open here
    # we could read it again but the file acts like a generator - it is exhausted stream is empty
# here file is automatically closed when we exit the with block
# there is no need to manually use close() method which avoids many errors

# let's print the first 200 characters of the text
print("First 200 characters of Rainis text: \n", rainis_text[:200])

# let's read all text as lines
# also we will use relative path
relative_rainis_path = Path("rainis.txt") # this means the file is in current working directory
# assert path exists
assert relative_rainis_path.exists(), "Rainis relative file path does not exist!"

# let's open the file and read all of it into a list of lines/rows
with open(relative_rainis_path, encoding="utf-8") as file:
    rainis_lines = file.readlines() # file.readlines() reads the whole file into a list of strings, potentially huge list
    # file is still open here
    # we could read it again but the file acts like a generator - it is exhausted stream is empty
    # we would need to use file.seek(0) method to reset the stream to the beginning
    # seek could be useful for some strange file formats - otherwise it is not needed
# here file is automatically closed when we exit the with block

# let's print all lines
print("All lines of Rainis text: \n", rainis_lines)
# note the \n in the end of each line - it is the newline character
# readlines() method does not remove the newline character
# why? because often we want to keep it - it is part of the text and maybe write it back to the file
# if you need to remove it you could use list comprehension
clean_rainis_lines = [line.strip() for line in rainis_lines] # line.strip() removes leading and trailing whitespace
print("All lines of Rainis text without newline characters: \n", clean_rainis_lines)

# we have one more method to read the file line by line
# we open the file then use for loop to read it line by line
# this is the most memory efficient way to read a file - works on HUUUUUGE files as long as they have lines
# let's read the file line by line and find lines that start with Kā 
ka_lines = []
with open(relative_rainis_path, encoding="utf-8") as file:
    for line in file: # file is a file stream object - it acts like a generator
        # here we read the file line by line - the file is not read into memory
        # we could process the line here
        print("Line: ", line.strip()) # line.strip() removes leading and trailing whitespace
        # i could do some processing here I could save the lines to another file
        if line.startswith("Kā"):
            ka_lines.append(line.strip())

# let's all print all lines that start with Kā
print(f"All lines of Rainis text that start with Kā: \n{ka_lines}")

# now that we have Kā lines let's write them back into a file
# i recommend using Path to create file name
ka_lines_path = Path("ka_lines.txt") # this means the file will be in the current working directory
# let's check if file already exists
if ka_lines_path.exists():
    print("Ka lines file already exists - it will be overwritten!")
    # i could avoid overwriting the file by using different name here 
else:
    print("Ka lines file does not exist - it will be created!")
    # i could put file writing code here

# let's open the file and write all Kā lines into it
with open(ka_lines_path, mode="w", encoding="utf-8") as file: # open() function opens the file in write mode
    # mode="w" means that the file will be overwritten if it already exists
    # mode="a" means that the file will be appended to if it already exists
    # mode="x" means that the file will be created if it does not exist otherwise it will raise an error
    # mode="r" is default and it is read mode
    for line in ka_lines:
        file.write(line + "\n") # file.write() writes a string to the file
        # if line does not have newline character we add it here, otherwise we would have double newline
        # here we write the line to the file
        # we could write the line to another file
    # we could keep writing here
# here file is automatically closed when we exit the with block

# let's try alternate approach and write everything all at once using join() method

file_name = "ka_lines_join.txt" # could skip Path here
# let's open the file and write all Kā lines into it

with open(file_name, mode="w", encoding="utf-8") as file: # open() function opens the file in write mode
    all_text = "\n".join(ka_lines) # "\n".join() joins all strings in the list with newline character
    # last line will not have newline character
    file.write(all_text) # file.write() writes a string to the file
    # here we write the whole text to the file
# here file is automatically closed when we exit the with

# so you can see how we might have not needed to strip the newlines from the lines

# now let's look at recipe that opens two files one for reading one for writing
# we will then go through the first file line by line and write the lines to the second file
in_file = Path("rainis.txt") # this means the file is in the current working directory
out_file = Path("rainis_filtered.txt") # this means the file is in the current working directory
# i could check here if the files exist and if they do I could ask the user if they want to overwrite them

# useful recipe for large files that do not fit into memory

# let's open the files and read from one and write to the other
with open(in_file, encoding="utf-8") as in_f: # open() function opens the file in read mode:
    print(f"Have opened {in_file} for reading")
    with open(out_file, mode="w", encoding="utf-8") as out_f: # open() function opens the file in write mode
        print(f"Have opened {out_file} for writing")
        for line in in_f: # this is the key line, we only read one line at a time, works on files that do not fit into memory
            if line.startswith("Kā"): # here use whatever logic for string filtering you want
                out_f.write(line) # here we write the line to the file
    # writing file is closed here but reading file is still open
# now everything is closed here

# last thing today is how to append to a file
# let's add something to rainis_filtered.txt
# how about a row of stars
# and then current date and time
# we will use open() function with mode="a" to append to the file AT THE END OF THE FILE ONLY
with open(out_file, mode="a", encoding="utf-8") as out_f: # open() function opens the file in append mode
    print(f"Have opened {out_file} for appending")
    out_f.write("*" * 80 + "\n") # here we write a row of 80 stars to the file
    out_f.write(f"Current date and time is: {datetime.now()}\n") # here we write the current date and time to the file

# append can only add to the end of the file!!
# if you need to insert earlier in the file you would need to read the whole file into memory
# then you would overwrite the file with the new content or create a new file with the new content

# if you need to add time_stamp to file name you could use strftime() method
# strftime() method is a method of datetime objects
file_with_time_stamp = Path(f"rainis_filtered_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt")
# adjust '%Y_%m_%d_%H_%M_%S' to your liking, could take some elements off or add more
print(f"Will write to file with time stamp: {file_with_time_stamp}")

# instead of writing let's just copy file using shutil module
# shutil module is a module for file operations

import shutil # this is how you import module - this is a standard library module could be up top 

# let's copy rainis_filtered.txt to file_with_time_stamp

shutil.copy(out_file, file_with_time_stamp) # shutil.copy() copies the file to the new location
# if file already exists it will be overwritten!

# there is also shutil.move() method that moves the file to the new location
# there is also copy2() and move2() that copy or move the file and preserve metadata like creation time