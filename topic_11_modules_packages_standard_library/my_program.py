# I am writing a program but I would like to use some functions from another file that I've written
# for that we use the import statement

# modules lets us use code that we have written in another file
# this is so called modular programming
# we can import the whole module or just a part of it

# usually imports are at the top of the file
import my_module # think of it as a giant copy paste of the file my_module.py
# generally we do not want to have modules that do anything when they are imported
# this is bad practice most of the time

# so those files that we plan to use as modules we want to have some code that will only run when the file is run directly

print("My program is running")