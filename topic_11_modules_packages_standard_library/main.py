import m_utils
# note that I do not need to import the math module, as it is imported in m_utils

print("Main script")
# let's try math first
# let's say factorial of 5
# if I have not imported math here i can use math from m_utils
print("Factorial of 5", m_utils.math.factorial(5))
# i could of course import math directly here and use it

result = m_utils.sum_prod([2,3],[5,10,2])
print(result)
# let's try with two ranges
result = m_utils.sum_prod(range(1,4), range(2,5), debug=True)
print("Result:", result)

# let's with unlimited number of sequences
numbers_1_12 = range(1,13)
result = m_utils.sum_prod_unlimited(numbers_1_12, range(2,5), range(10,13), debug=True)