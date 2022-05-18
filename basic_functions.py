def say_hello():
    print('hello')
    print('how')
    print('are you')

say_hello()

#passing arguments
def say_hello2(name):
    print(f'Hello {name}')

say_hello2('Pawel')

#if the name is not provided, you can add definition  to the name as default
def say_hello3(name="Sir"):
    print(f'Hello {name}')

say_hello3()


#functions have rutun not much pring
#IMPORTANT return lets you assign to variable

def add_num (num1,num2):
    return num1 + num2

result = add_num(1,4)
print(result)

#This returns a NoneType type because it is a print not the return
#This perfroms the action in place not returning anything
def add_num2 (num1,num2):
    print(num1 + num2)

#This part does not execute because the result cannot be assigned to a print

result = add_num2(1,4)
print(result)

#Make sure to check for types just in case strings are passed correctly
#Python is dynamiclly typed, that means we dont need to specify type

def add_num3(num1, num2):
    return(num1 + num2)

print('This should return two numbers added together')
print(f'Passing a 10 and 20 as string gives us: {add_num3("10", "20")}')
print(f'Passing a 10 and 20 as numbers gives us: {add_num3(10, 20)}')
