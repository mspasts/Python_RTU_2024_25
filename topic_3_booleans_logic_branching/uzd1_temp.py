"""
1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
Ja ir pāri 37, tad izvadiet "iespējams drudzis"
"""

temperature = float(input("lūdzu ievadiet savu temperatūru "))
# if temperature < 35:
#     print("nav par aukstu ?")
# elif 35 <= temperature <= 37: #same as 35 <= temperature and temperature <= 37
#     print("viss kārtībā")
# else: # here over 37
#     print("Iespējams drudzis")

# alternativs risinājums - tāds pats rezultāts, drusku cita loģika

if temperature < 35:
    print("nav par aukstu ?")
elif temperature > 37:
    print("Drudzis")
else: # 35 <= temperature <= 37
    print("ir ok")