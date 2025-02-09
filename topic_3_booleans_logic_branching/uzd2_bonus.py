"""
2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.
Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.
Izvadiet bonusu.
Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
"""

MINIMUM_YEARS = 2 # i could use lowercase, but UPPERCASE in Python signifies constant values
BONUS_RATE = 0.15
name = input("What is your name?")
print("What is your salary?")
 
salary = input("Salary is ")
salary = int(salary) # could be float maybe
print(f"Thank You, {name}")
print(f"How many years do You work for the company?")
years = input("I work ")
years = int(years)
if years > MINIMUM_YEARS:
    bonus_years = years - MINIMUM_YEARS
    # Bonuss 15% no algas par katru gadu
    bonus = salary * BONUS_RATE * bonus_years
 
    print("Oh wow! So long with us?")
    print(f"Congrats! You'll have a surprise for Christmas - {bonus} - bonus for your contribution")
else:
    print("Merry Christmas and a Happy New Year! Have a nice holiday and see you next year!!")