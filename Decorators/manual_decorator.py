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
