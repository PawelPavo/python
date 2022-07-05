from collections import namedtuple

# Calling tuple by index
mytuple=(10,20,30)
print(mytuple[0])

# If we have a huge tuple with many INDEXES we can use Named-Tuple

# Creating NAMED Tuple - looks like OOP classes
Dog=namedtuple('Dog',['age','breed','name'])
sammy=Dog(age=5,breed='Husky',name='Sam')

print(type(sammy))

# Thses are the same outputs
print(sammy.age)
print(sammy[0])
