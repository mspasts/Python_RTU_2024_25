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
    # rainis path could be a string or Path object
    # we uses encoding="utf-8" to specify that the file is in UTF-8 encoding, these days this is 99% of the time
    # default is read mode
    rainis_text = file.read() # file.read() reads the whole file into a string, potentially huge string
    # file is still open here
# here file is automatically closed when we exit the with block

# let's print the first 200 characters of the text
print("First 200 characters of Rainis text: \n", rainis_text[:200])