import string

# Vai ir pangramma?

def is_pangram(buramvardi, alphabet=string.ascii_lowercase):
    '''
    Checks if the input string is a pangram.
    Pangram is a sentence that contains every letter of the alphabet at least once.
    param buramvardi: string to check
    param alphabet: string containing the alphabet to check against
    return: True if the input string is a pangram, False otherwise
    '''
  
    # buramvardi = set(buramvardi.lower().replace(" ", ""))
    buramvardi = set(buramvardi.lower()) # no need to get rid of whitespace
    alphabet = set(alphabet.lower())
    
    
    # return all(char in buramvardi for char in alphabet)
    # above works but is a bit hard to read
    return buramvardi >= alphabet
 
latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
# assert we use for testing basic assumptions about our code
# useful for catching bugs early
assert len(latvian_alphabet) == 33, "tas nav latviešu alfabēts"
# assert does nothing if the condition is True
 
print(is_pangram("Cepts Cālis Caurā Pannā", "aābcčdeēfgģhiījkķlļmnņopqrsštuūvzž"))  
print(is_pangram("AĀBCČDEĒ", "abc")) 
print(is_pangram("Meža Veči Egli Nes", "eži"))  

# let's try English
print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
# boxing wizards jump quickly
print(is_pangram("boxing wizards jump quickly")) # False
# there is a longer version of boxing wizards

# latvian pangram would be:
# "Četri balti krekli ar melnu piedurkni zilā krūšturī" - hallucination
print(is_pangram("Četri balti krekli ar melnu piedurkni zilā krūšturī", latvian_alphabet)) # True

hipiji = "Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku"
print(is_pangram(hipiji, latvian_alphabet)) # True
