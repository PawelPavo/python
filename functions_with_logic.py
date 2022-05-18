def even_check(num):
    result = num % 2 == 0
    return result

print(even_check(20))


#You can return the equestion, no need to assign the var

def even_check2(num):
    return num % 2 == 0

print(even_check2(21))


#returns true if any number is even inside list

#the "return False" is at the for-loop level because the loop needs to check all the numbers
#if it was placed where the "pass" is, it would break after 1st loop
#because both conditions return call on both conditions
#you want to check all the numbers before returning False

#has at least one even number in the list
def check_even_list(num_list):
    for  num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

print(check_even_list([1,3,5,7]))
print(check_even_list([2,4,6,8]))
print(check_even_list([1,3,8,7]))

#same as above but return the even numbers in a list

def return_even_list(num_list):
    even_nums=[]
    for  num in num_list:
        if num % 2 == 0:
            even_nums.append(num) 
        else:
            pass
    return even_nums

print(return_even_list([1,3,5,7]))
print(return_even_list([2,4,6,8]))
print(return_even_list([1,3,8,7]))


