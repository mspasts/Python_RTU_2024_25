"""
3. Uzdevums - Celsijs uz Farenheitu
Uzrakstiet programmu, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc
Farenheita skalas.
farenheit = 32+celsium*(9/5)
"""

# This program converts a temperature from Celsius to Fahrenheit with error handling
print("Programma, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc Fārenheita skalas")

while True:
    try:
        # Prompt the user to enter the temperature in Celsius
        temperature_celsius = float(input("Type temperature in Celsius: "))

        # Convert the temperature to Fahrenheit
        temperature_fahrenheit = 32 + temperature_celsius * (9 / 5)

        # Print the temperature in Fahrenheit with 2 decimal places
        print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}")

        # Alternatively, round the temperature to 2 decimal places
        PRECISION = 2
        tf = round(temperature_fahrenheit, PRECISION)
        print(f"Rounded temperature in Fahrenheit: {tf:.2f}")

        break

    except ValueError:
        print("Invalid input! Please enter a valid number for the temperature in Celsius.")
