# tātad int mēģina pārvērst kādu datu tipu uz int - veselo skaitli
my_integer = 42
print(my_integer, "is of data type", type(my_integer))
casted_to_int = int(my_integer) # works but not much point
print(casted_to_int, "is of data type", type(casted_to_int))
MY_PI = 3.1415926 # we typically use upperase for constants - not real constants
print(MY_PI, "is of data type", type(MY_PI))
american_pi = int(MY_PI)
print(american_pi, "is of data type", type(american_pi))
# so technically works kind of like floor for positive values
MY_E = 2.7181
print(MY_E, "is of data type", type(MY_E))
american_e = int(MY_E)
print(american_e, "is of data type", type(american_e))
# compare with round
rounded_e = round(MY_E) # will give us integer but rounded so down or up
print(rounded_e)

# int can be
my_string = "90210"
my_string_into_int = int(my_string) # this works since string contains only numbers
print(my_string_into_int, type(my_string_into_int))
# we can not cast string directly into int if it has float like number
string_float = "3.5252626" # we can not cast directly into int
# string_float_into_int = int(string_float) # this will raise Error
# # so 25 needs to be handled differently



