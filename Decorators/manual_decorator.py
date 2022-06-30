'''
def func():
    return 1


# Tells you that there is a functin but not execute it
print(func)

# executed function
print(func())


# re-assign a function example
def hello():
    return 'Hello!'


greet = hello
print(greet())

# this will work if the 'hello' function is deleted
greet2=hello
del hello

print(greet2())

'''

def hello(name='Pawel'):
    print('The hello() function has been executed.')

    # greet and welcome are in hello() scope - they cannot be called outside of hello()
    # but we can make hello() return functions 
    def greet():
        return '\t This is a greet() function inside hello.'

    def welcome():
        return '\t This is welcome() function inside hello.'

    # EXECUTING FUNCTIONS
    # we used print because the functions have return 'str', so we want to see it
    '''
    print(greet())
    print(welcome())
    print('This is the end of the hello() function'
    '''
    # RETURNING FUNCTION
    print('I am going to return function!')
    if name == 'Pawel':
        return greet
    else:
        return welcome

# This is the assigning functin 
my_new_func = hello('Pawel')

# This will fire the actual greet()
print(my_new_func())

# EXAMPLE 2

def cool():
    def super_cool():
        return 'I am very cool'
    return super_cool

some_func = cool()
print(some_func())
