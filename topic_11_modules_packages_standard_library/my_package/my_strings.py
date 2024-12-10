# let's have some string functions

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    # let's strip spaces and make it lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1] 