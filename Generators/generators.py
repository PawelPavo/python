# Createing generators

# Regular example
def create_cubes(n):
    result=[]
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

for x in create_cubes(10):
    print(x)

print('\n')
print('========== BREAK ==========')
print('\n')


# GENERATOR transformation

# This is generator
def create_cubes_2(n):
    for x in range(n):
        yield x**3

# This does not print the list like above,
# we need to cast a generator to a list
print(create_cubes_2(10))
print(list(create_cubes_2(10)))

for x in create_cubes_2(10):
    print(x)

