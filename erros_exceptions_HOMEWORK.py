# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('This is not the correct type of input. In order to perform SQRT, we need numbers.')



# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('You cannnot divide by zero!')
finally:
    print('All Done!')


# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def give_me_int():
    while True:
        try:
            result=int(input('Please provide and integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is: {}'.format(result**2))
            break

give_me_int()


# Diffrent way Problem 3

def ask():
    # Waiting for correct response
    waiting=True
    while waiting:
        try:
            res=int(input('Enter a number: '))
        except:
            print('Error. Please try again! \n')
            continue
        else:
            waiting=False # You dont need a break if you are using a variable T/F in a while loop
            
    print('Your number sqaured is: ')
    print(res**2)

ask()


