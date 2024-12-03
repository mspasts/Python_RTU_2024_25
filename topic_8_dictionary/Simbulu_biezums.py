# 1a

def get_char_count(text):
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1 # add to existing
        else:
            char_dict[char] = 1 # create new entry
        # same as
        # char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict
print(get_char_count("hubba bubba"))

# 1b

def get_digit_dict(num):
    num_str = str(num)
    rezultats = {}
    for cipars in '0123456789': # so we go through 10 digits
        rezultats[cipars] = num_str.count(cipars) # count hides a loop 
    return rezultats # if you think about it for digit dictionary count could have used a list with index 0 to 9
print(get_digit_dict(599637003))

# we could have imported Counter from collections and used it to get the same result
from collections import Counter
my_counter = Counter("hubba bubba")
print(my_counter)
digit_counter = Counter(str(599637003)) # we can pass a string to Counter
print(digit_counter)