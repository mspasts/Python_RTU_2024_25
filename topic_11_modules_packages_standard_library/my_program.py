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

# since we imported my_module we can use anything that is defined in that file
# we have gained so called namespace
# so we avoid polluting the global namespace

# i can print MY_PI from my_module
print("Value of PI from my_module:", my_module.MY_PI)

my_module.print_my_shopping_list(my_module.my_shopping_list)

# i could have my own shopping list
another_list = ["milk", "bread", "eggs"]
my_module.print_my_shopping_list(another_list)

my_zebra = my_module.Pet("Marty", "zebra")
print(my_zebra)
print(my_zebra.get_sound("neigh"))

# i could make more pets now
my_fish = my_module.Pet("Nemo", "fish")
print(my_fish)
print(my_fish.get_sound("blub"))

# so why use modules?
# - to organize code
# - to reuse code
# - to avoid name conflicts
# - to make code easier to read

# downsides
# - can be slower to import - usually not an issue
# - can be harder to debug - usually not an issue
# - can be harder to understand - usually you should not need to understand the whole module