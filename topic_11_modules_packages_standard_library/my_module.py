# so let's come up with some functions and variables that we can use in our program
# also I can put in classes in my module
# Python modules are just Python files that contain definitions and statements. The file name is the module name with the suffix .py appended.
# the file name can be anything like regular .py file

# print("My module is active!")  # usually we do not want this to run when we import the module

my_shopping_list = ["apples", "bananas", "pears"]
my_number = 42
# variables are also less often used in modules
# sometimes things like constants are use
MY_PI = 3.1415926 # by convention constants are written in all caps, but not enforced by Python

# functions in modules should not depend on anything besides inputs and should not change anything outside of the function
# some function

# good practice would be to have docstrings for functions that you write for importing by others
# also add type hints whenever they make sense

def print_my_shopping_list(my_list):
    """
    This function prints a shopping list
    :param my_list: list of items
    :return: None
    """
    print("I need to buy:")
    for item in my_list:
        print(item)


# another function
def my_adder(a, b):
    """	
    This function adds two numbers
    :param a: number
    :param b: number
    :return: sum of a and b
    """
    return a + b

# a class for pet
class Pet:
    """
    This class represents a pet
    We could write more about it here
    """
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    # make a sound
    def get_sound(self, sound:str) -> str:
        """
        This method makes a sound
        :param sound: str
        :return: str
        """
        return f"{self.name} says {sound}"


# let's use __main__ to run some code when the module is run
# now I can use this for a script or for testing my module
# I could do nothing as well if I do not want to run anything
if __name__ == "__main__":
    print("My module is active!")
    print("This will only run when the module is run directly")
    my_cat = Pet("Fluffy", "cat")
    my_dog = Pet("Rex", "dog")
    print(my_cat.get_sound("meow"))
    print(my_dog.get_sound("woof"))
    print_my_shopping_list(my_shopping_list)
    # i could add some tests here
    # this is a good practice to have tests in your module
    # let's test adder
    assert my_adder(2, 2) == 4, "Test failed!" # again if assertion is True NOTHING happens
    assert my_adder(-3, 3) == 0, "Test failed!" # if assertion is False then AssertionError is raised
