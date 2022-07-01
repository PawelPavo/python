import random

print('=========== Q1 ===========')
# Create a generator that generates the squares of numbers up to some number N.

def gen_square(n):
    for num in range(n):
        yield num**2

print(list(gen_square(10)))
for num in gen_square(10):
    print(num)

print('=========== Q2 ===========')

# Create a generator that yields "n" random numbers between a low and high number(that are inputs).

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


print('=========== Q3 ===========')

#Use the iter() function to convert the string below into an iterator:

s = 'hello'
s_i = iter(s)

print(next(s_i))
print(next(s_i))
print(next(s_i))
print(next(s_i))
print(next(s_i))
