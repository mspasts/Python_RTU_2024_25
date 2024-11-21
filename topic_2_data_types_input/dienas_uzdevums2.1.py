print("Ši programma noprasa un saglabā lietotāja vārdu")
name = input("What is your name, friend? ")
print(f"Name {name} saved")
age = input(f"What is your age , {name}? ")
age = float(age)
age_to_100 = 100 - age
rounded_age = round(age_to_100)
print (f"You will be 100 years old in {rounded_age} years")
birthyear = input("What year were you born, {name}?")
hundred_years_old = float(birthyear) + 100
print (f"You will be 100 years old in year {hundred_years_old}")