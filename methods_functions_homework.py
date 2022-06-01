import math
import string 

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

def up_low(s):
    lower=0
    upper=0
    punc=0
    for x in s:
        if x in string.punctuation:
            punc+=1
        elif x == ' ':
            punc+=1
        elif x.isupper()==True:
            upper+=1
        else:
            lower+=1
    return lower,upper

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))

def up_low_2(s):
    lower2=0
    upper2=0
    for x in s:
        if x.isupper():
            upper2+=1
        elif x.islower():
            lower2+=1
        else:
            pass
    return lower2,upper2

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low_2(s))

#solution
def up_low_solution(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low_solution(s)



#Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(lst):
    new_list = list(set(lst))
    return new_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


#solution - the set() is correct


def unique_list_solution(lst):
    new_list=[]
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list

print(unique_list_solution([1,1,1,1,2,2,3,3,3,3,4,5]))


#Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    result=1
    for x in numbers:
        result=result*x
    return result

print(multiply([1,2,3,-4]))

#solution

def multiply_2(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply_2([1,2,3,-4]))


#Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    return s.replace(' ','')[::-1]==s.replace(' ','')

print(palindrome('nurses run'))
print(palindrome('abcba'))

#solution

def palindrome_2(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing


print(palindrome_2('nurses run'))
print(palindrome_2('abcba'))



#Write a Python function to check whether a string is pangram or not.
#(Assume the string passed in does not have any punctuation)



