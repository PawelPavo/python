import math


# List of math functions 'math' provides
'''
help(math)
'''

# Rounding
value=4.75

print(math.floor(value))
print(math.ceil(value))

# math mod is not needed for round its native to python
print(round(value))

# In Python, if the fractional component of the number is halfway between two integers,
# one of which is even and the other odd, then the even number is returned.
# This kind of rounding is called rounding to even (or banker’s rounding)
print(round(4.5))
print(round(5.5))
