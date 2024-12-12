# now that we have installed matplotlib, we can test it

# first let's try importing it
try:
    import matplotlib.pyplot as plt
    # note that we are importing pyplot module from matplotlib package with an alias plt
    print("matplotlib is installed")
except ImportError:
    print("matplotlib is not installed")
    print("Please install matplotlib by running: pip install matplotlib")
# of course usually we know that we have installed it, but it is good to check

# let's create a simple sine wave plot
# let's use regular python lists for x and y values
import math
# let's use list comprehension to create x values from 0 to 10 in steps of 0.1
x = [i/10 for i in range(100)]  # values from 0 to 10 in steps of 0.1
y = [math.sin(i) for i in x]  # sine of each value in x
# let's print first 5 values of x and y
print("First 5 values of x:", x[:5])
print("First 5 values of y:", y[:5])

# let's plot x and y
plt.plot(x, y)
plt.title("Sine wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show() # to see the plot