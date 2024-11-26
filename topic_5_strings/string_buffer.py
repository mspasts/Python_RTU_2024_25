# there is this idea of building up buffer for string
# when processing
buffer = ""
supper = "Kartupeļi ar siļķi"
# I could use replace
a_to_A = supper.replace("a", "A")
print(a_to_A)
# i could use buffer to build a new string instead
# this is for complex cases
for char in supper:
    # we could add more complex logic here
    if char == "a":
        buffer += char.upper()
    else:
        buffer += char
print(buffer)