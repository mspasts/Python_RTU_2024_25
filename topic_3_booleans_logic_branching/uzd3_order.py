"""
3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām
Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
"""

# 3. Uzdevums - Kārtībai jābūt
X = int(input("1. skaitlis: "))
Y = int(input("2. skaitlis: "))
Z = int(input("3. skaitlis: "))
if X <= Y and Y <= Z:
    print(X, Y, Z) # tas sanāk, ka if ir vienīgais gadījums, kad viss sakārtojas pats par sevi..
elif X <= Z and Z <= Y:
    print(X, Z, Y)
elif Y <= X and X <= Z:
    print(Y, X, Z)
elif Y <= Z and Z <= X:
    print(Y, Z, X)
elif Z <= X and X <= Y:
    print(Z, X, Y)
elif Z <= Y and Y <= X:
    print(Z, Y, X)
# pārējos ir jāspēlējas ar cipariņiem, lai izdomātu, kā sakārtot, piemēram, 3, 7 un 9; 9, 3 un 7; 7, 9 un 3 utt.