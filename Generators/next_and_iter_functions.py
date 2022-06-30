# This is Next function and Iter function

def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

g=simple_gen()
print(g)

# NEXT() function

# Next displayed the next number in the for-loop and displays it
# For-Loop doesnt error becasue it has a error handler
print(next(g))
print(next(g))
print(next(g))
print('This error is intentional')
# this will error because there are only 3 number 0,1,2
#print(next(g)) # this will error because there are only 3 number 0,1,2



# ITER() function

s='hello'
for letter in s:
    print(letter)

print('\n')
print('========= BREAK =======')

# this will not work
#print(next(s))

# we need to assign iter() to the s
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
