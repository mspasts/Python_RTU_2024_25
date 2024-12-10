# once we know how to use a module we can start using packages
# packages are simply directories with modules
# they can even include other packages (other directories)
# a bit simplified but that's the idea

# so I have a folder called my_package
# it has three modules my_math.py and my_strings.py and let's go with pet.py for Pet class

# let's import my_math
import my_package.my_math as mm # very typical to use abbreviation for the module name
# now I can use the module from my_package directly with mm
print("Addition:", mm.add(1, 2))
print("Subtraction:", mm.subtract(5, 3))

# i could import my_strings
import my_package.my_strings as ms
print("Reversed string:", ms.reverse_string("hello"))

# how about Pet class?
# i could import full module
# import my_package.pet
# my_zebra = my_package.pet.Pet("Marty", "zeebra")
# # note that I need to put my_package.pet.Pet because Pet is in pet module
# print(my_zebra)

# this time I will import without alias
from my_package.pet import Pet # this could potentially cause name conflict with Pet class from another module
my_zebra = Pet("Marty", "zebra")
print(my_zebra)
print(my_zebra.get_sound("neigh"))