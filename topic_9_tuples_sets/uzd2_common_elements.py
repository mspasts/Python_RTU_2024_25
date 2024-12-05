# Kopējie Elementi
def get_common_elements(seq1, seq2, seq3):
 
    virkne1 = set(seq1)
    virkne2 = set(seq2)
    virkne3 = set(seq3)
    
    return tuple(sorted(virkne1 & virkne2 & virkne3))

print(get_common_elements("bumbieris", ['b','u','m','b','a'], ('r','u','m','b','a')))  
print(get_common_elements("abcd", ['a','b','d'], ('b','c','d'))) 