#Lietotājs un tā vecums
TARGET_AGE = 100 # it could come from database, or file, or somewhere else
# try to avoid magic numbers in your main code
username = input("Please enter your username? ")
print(f"Welcome ", username)
user_age = input("How old are you? ")
print(f"Hey {username} ->", user_age, "that's rly not that old :)")
user_age = int(user_age)
target_years = TARGET_AGE - user_age
print("But in -> ", target_years, f"years you will become {TARGET_AGE} and that is one old {username} :P")
# from datetime import date
# today = date.today()
# year = int(today.strftime("%Y"))
import datetime
year = datetime.datetime.now().year
print("Year is: ", year)
year_of_birth = year - user_age
print("Means you were born in ", year_of_birth)