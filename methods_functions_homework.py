import math

#Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4/3)*(math.pi)*(rad**3)


# Check - solution from the book uses 3.14 as pi
print(vol(2))




#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    for x in range(low,high+1):
        if num == x:
            print(f'{num} is in range {low} and {high}')
        
# Check
ran_check(2,2,7)


#If you only wanted to return a boolean:

def ran_bool(num,low,high):
    if num in range(low, high+1):
        print(True)

#check
ran_bool(3,1,10)

#Solution

def ran_check_solution(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')
        
# Check
ran_check_solution(2,2,7)

def ran_bool_solution(num,low,high):
    return num in range(low,high+1)
print(ran_bool_solution(3,1,10))



#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


