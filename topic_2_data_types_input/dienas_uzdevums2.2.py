width = input("What is width of room? ")
lenght = input("What is lenght of room? ")
height = input("What is height of room? ")
width_int = float(width)
lenght_int = float(lenght)
height_int = float(height)
volume = width_int * lenght_int * height_int
print (f"Volume of room is {volume} m³")
print (f"Volume of room is {volume:15.2f} m³") # so show only 2 digits after comma
# so 15 says I want 15 spaces total for my volume output
# but only 2 for the digits after comma