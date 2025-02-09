"""
Uzrakstiet programmu, kas noprasa un saglabā lietotāja vārdu
Uzdod jautājumu par lietotāja vecumu, jautājumā izmantojot lietotāja vārdu.
Uzrāda pēc cik gadiem lietotājam būs 100 gadi :)

BONUS: Lai programma uzrādā arī gadu kad lietotājam būs 100 gadi. Tam varētu izmantot mainigo ar patreizējo gadu.
Vēl labāk būtu iegūt patreizējo gadu automātiski tad Jums vajadzēs divas papildu rindiņas:
import datetime # par importiem runāsim atsevišķi
currentYear = datetime.datetime.now().year
"""
import datetime
# Get the current year
currentYear = datetime.datetime.now().year

# Ask user for their name and save it
print("Ši programma noprasa un saglabā lietotāja vārdu")
name = input("What is your name, friend? ")
print(f"Name {name} saved")

# Ask user for their age and calculate when they will be 100 years old
age = float(input(f"What is your age , {name}? "))
age_to_100 = 100 - age
rounded_age = round(age_to_100)
print (f"You will be 100 years old in {rounded_age} years")

# Ask user for their birthyear and calculate when they will be 100 years old
birthyear = currentYear - age
hundred_years_old = birthyear + 100
print(f"Your were born in {int(birthyear)}")
print (f"You will be 100 years old in year {int(hundred_years_old)}")