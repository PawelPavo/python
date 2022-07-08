import math
import random

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

print('=========== RANDOM ===========')

# Random
myval=random.randint(0,100)

print(myval)

print('========== SEED ==========')

# SEED is to get the same number through random for testing or other
'''
random.seed(101) # this can be any num but coder use 101 cause its nice or 42 from Hitchhiker's guide to the galaxy
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
'''

print('========= LIST RANDOM CHOICE =========')
# Grabbing random object from the list

mylist=list(range(0,21))

# grabbing one
print(mylist)
print(random.choice(mylist))

# grabbing multi
# SAMPLE WITH REPLACEMENT - can choose the some object
print(random.choices(population=mylist,k=10)) # k is not a random choice

# SAMPLE WITHOUR REPLACEMENT - cannot choose the same object again
print(random.sample(population=mylist, k=10))


