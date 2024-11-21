print("Programma, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc Fārenheita skalas")
temperature_celsius = input("Type temperature in Celsius? ")
temperature_farenheit = 32+float(temperature_celsius)*9/5
print(f"temperature in farenheit {temperature_farenheit:.2f}")
# alternative round to 2 digits with
PRECISION = 2
tf = round(temperature_farenheit, PRECISION)