from collections import defaultdict

d = {'a':10}
print(d['a'])

# Normal dictionary
# Gives an error when you try to use a key that does not exist
# example:
'''
print(d['WRONG'])

'''
# CHECKING dictionary
print(d)

# DEFAULT DICTIONARY will assign a default value when needed and not error
# for example when we use a for loop to add keys that are not present in the dictionary
# it assigns a defualt when the KEY ERROR would occure

# lambda we assign the default value to the keys that defaultdict creates
c =  defaultdict(lambda:'default value')
c['correct']=100
print(c['correct'])

# this will not error now because of 'defaultdict'
print(c['WRONG KEY'])
print(c['WRONG KEY'])
# CHECKING dictionary
print(c)
