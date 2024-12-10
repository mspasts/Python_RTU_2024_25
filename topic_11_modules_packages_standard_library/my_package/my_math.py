# let's have some math functions
# again this module should not do anything when imported

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# if I wanted tests I would put them behind main guard
if __name__ == "__main__":
    print("Running tests")
    assert add(1, 2) == 3, "Test 1+2 failed"