height = int(input("Ievadiet eglītes augstumu: "))

for i in range(1, height + 1):
    # Aprēķinām atstarpes un zvaigznes skaitu katrā rindā
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
# let's add a leg
leg_spaces = (height-1) * " "
leg_string = leg_spaces + "||"
# if we do not need the variable we use _ in Python
# we do this when we want to repeat something without need for variable itself

for _ in range(3):
    print(leg_string)

#Eglīte
 
i = 1 #definējam pirmo rindiņu jeb cik zvaigznīšu būs šeit un no kurienes sākt ciklam izpildīties 
n = height #n = rindiņu daudzums jeb eglītes augstums
while i <= n: #cikls turpinās, kamēr i nepaliek mazāks vai vienāds ar n t.i. 10 
    space_cnt = n - i # šeit mēs izveidojam nosacījumu atstarpēm lai zvaigznītes nebūtu viena zem otras bet gan veidotu piramīdu
    star_cnt = 2 * i -1 #šeit mēs aprēķinām nepāra skaitli atstarpēm piemērām 2*1=2, 2-1=1 utt., ja i sāktos ar pāra skaitli piemēram 2 tad formula būtu 2 * i + 1
    print(" " * space_cnt + "*" * star_cnt) 
    i += 1 # nosakām ka cikls izpildoties liks klāt vienu rindiņu līdz netiks izpildīti while nosacījumi


# functions soon :)
# def print_tree(height):
#     for i in range(1, height + 1):
#         # Aprēķinām atstarpes un zvaigznes skaitu katrā rindā
#         spaces = " " * (height - i)
#         stars = "*" * (2 * i - 1)
#         print(spaces + stars)
# 
# # Ievadām eglītes augstumu
# height = int(input("Ievadiet eglītes augstumu: "))
# 
# # Izdrukājam eglīti
# print_tree(height)