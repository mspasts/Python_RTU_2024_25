# I am writing a program but I would like to use some functions from another file that I've written
# for that we use the import statement

# modules lets us use code that we have written in another file
# this is so called modular programming
# we can import the whole module or just a part of it

# usually imports are at the top of the file
# import my_module # think of it as a giant copy paste of the file my_module.py
# # generally we do not want to have modules that do anything when they are imported
# # this is bad practice most of the time

# # so those files that we plan to use as modules we want to have some code that will only run when the file is run directly

# print("My program is running")

# # since we imported my_module we can use anything that is defined in that file
# # we have gained so called namespace
# # so we avoid polluting the global namespace

# # i can print MY_PI from my_module
# print("Value of PI from my_module:", my_module.MY_PI)

# my_module.print_my_shopping_list(my_module.my_shopping_list)

# # i could have my own shopping list
# another_list = ["milk", "bread", "eggs"]
# my_module.print_my_shopping_list(another_list)

# my_zebra = my_module.Pet("Marty", "zebra")
# print(my_zebra)
# print(my_zebra.get_sound("neigh"))

# # i could make more pets now
# my_fish = my_module.Pet("Nemo", "fish")
# print(my_fish)
# print(my_fish.get_sound("blub"))

# # so why use modules?
# # - to organize code
# # - to reuse code
# # - to avoid name conflicts
# # - to make code easier to read

# # downsides
# # - can be slower to import - usually not an issue
# # - can be harder to debug - usually not an issue
# # - can be harder to understand - usually you should not need to understand the whole module

# I can import module with a name that I choose - an alias
# import my_module as mm # very typical to use abbreviation for the module name
# # so my_cool_module would be mcm
# # there is a possibility to have name conflicts so we can use alias to avoid that

# # now I can use mm instead of my_module
# mm.print_my_shopping_list(mm.my_shopping_list)
# print("MY PY", mm.MY_PI)

# above would be my recommended way of importing modules
# either full import or with alias

# we have more specific imports
# we use these when we only need a specific function or class from the module
# this can be useful for LAAAARGE modules

# let's import my_adder from my_module
# let's also import MY_PI
# we separate imports with commas when we import multiple things from single module

from my_module import my_adder, MY_PI # now I can use my_adder without the module name
print(my_adder(2, 3))
print("Value of PI:", MY_PI)
# # of course we should be careful with this in case there is some name conflict in global namespace

# in case of some name conflict we can use alias for specific import
# from my_module import my_adder as my_super_duper_adder
# print(my_super_duper_adder(2, 3))

# lastly there is one method of importing that I would recommend to avoid
# this is so called wildcard import - some people like it but I think it is bad practice
# from my_module import * # this will import everything from my_module INTO global namespace
# with this approach I lose fine grained control over what is imported
# also I lose namespace which can lead to name conflicts
