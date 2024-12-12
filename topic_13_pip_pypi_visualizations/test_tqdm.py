# let's test our newly installed tqdm package
# tqdm is a package that allows you to create progress bars
# it is an external package that is not included in the standard library

try:
    from tqdm import tqdm
    print("tqdm is installed")
except ImportError:
    print("tqdm is not installed")
    print("Please install tqdm by running: pip install tqdm")

# Let's create a progress bar
for _ in tqdm(range(10_000_000)):
    pass

counter = 0
for _ in tqdm(range(10_000_000)):
    counter += 1
print("Counter:", counter)