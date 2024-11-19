# In Python we use # for comments, lines with # will be ignored by Python interpeter
print("Hello November Pythonists!") # I can write comment here too at end of instruction
print("Pasmaidīsim 😀")
# i can leave a line empty if I want

# let's try to break things
print("     Kur tu teci Gailīti manu?")
# i can use single quotes - in Python they work identically
print('Jāmaina ziemas riepas, vai ne?') # so if I start with ' then end string with '
# so use " if you need ' inside the text string
print("It's a nice day, isn't it?")
# vice versa we can use ' outside to have " inside
print('Alice said "follow the rabbit" and ran after it')
# let's do a little bit of math
print(2+2)
# compare with
print("2+2")
# let's print two different things at once
print("3*3=",3*3) # first item is a string, second an integer
# we can subtract
print("10-5 =",10-5) # the single space comes as default from comma
# it can be changed
# we also have really cool syntax to put expressions inside strings
print(f"10*2-6={10*2-6}") # the expression inside { } will be evaluated
# above is called f-string useful to create templates for text

# we can use parenthesis for changing order
print("(3+4)*5=",(3+4)*5)
# we have some interesting things with division
print("20/6=", 20/6)
# we got our so called float - floating point number (technically double precision)
# they are very convenient but
# in Python they lose precision at around digit 16
# more on this who want to go to sleep: https://en.wikipedia.org/wiki/IEEE_754
# some numbers are impossible to show exactly in floating point standard
# one example is 0.1

# now back to normal math
print("20//6=", 20//6) # returns integer part of the division
print("20%6=", 20%6) #modulo operator, for positive numbers same as reminder - atlikums

print("18%2 = ? ", 18%2)
print("19%2 = ? ", 19%2)
print("20%2 = ? ", 20%2)

# Python has built in support for laaaarge numbers
# also ** is power operator
print("2**3=", 2**3)
print("2**4=", 2**4)
print("2**8=", 2**8) # so 2 to the power of 8
print("2**16=", 2**16)

# for square roots we can use 0.5 (or also math library)
print("√9= ?", 9**0.5) # note result is float even though here it is whole
print("√2= ?", 2**0.5) # note imprecision in the end
print("2to the -3", 2**(-3)) # 0.125 1/8

# back to big numbers
print("2**32", 2**32)
# now we moved onto 64 bit systems so we can address more memory..
print("2**64", 2**64)
# how about number of atoms in universe say 10 to 78 ?
print("10**78", 10**78)

# last thing for today we can multiply strings surpisingly but not add string and number
# we can add / concatenate strings
print("Valdis" + " likes Python")
# print("Valdis" + 2024) not possible we need 2024 to be string with str(2024)

print("Beer 🍺 "*5)
# good for things like
print("*"*40)



