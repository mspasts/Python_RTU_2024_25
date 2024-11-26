height = 5

for i in range(height):
    print(" " * (height - i - 1) + "*" * (i + 1))
    
print(" " * (height - 1) + "*")
    
height = 4

print("   ^   ^   ")

print("  / * * * \\")

for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))
    print("    | |    ")