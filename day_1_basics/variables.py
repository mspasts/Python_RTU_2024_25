# we have some data that we want to use multiple times
print("Mēs sākam programmu")
# in Python we need no special permission to make a variable
# most other languages use keywords let, const, var, val, etc.
name = "Kaķis" # name is an identifactor for a variable pointing to string "Valdis"
print(name)
# compare to
print("name") # this is just a string not a variable

print("Hello there", name)
# name = "Līga" # Python lets us redefine variable at any point
print(name *5)

#  
# print("Ba" +"na"*2)
print("some name * 7", name*7)

# print("60*60*24*366", 60*60*24*366)
# it can be a good idea to give descriptive names to data
seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 366 # note how this is the only one that could change
print("Seconds in current year 2024")
print(seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year)
# in short code, seconds, minutes, hours, days would be better


# here we use Pythonic style for variables
# we use _ to separate multiple word variables
# what can be variable identificator?
# start with lower or upper case letter
# then letters, numbers, underscores
# AVOID non english leters
# do not do this
kaķis = "Vinnijs" # bad variable name for non Latvian speakers...
# kakis would be less bad
# cat_name is better variable name than kaķis ...
cat_name = "Dārcijs" # variable values can be anything
print(kaķis, cat_name)

