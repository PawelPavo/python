#SPY GAME:
#Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(arr):
    my_arr=[]
    for i in arr:
        if i == 0 or i==7:
            my_arr.append(i)
        if my_arr==[0,0,7]:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#Solution

def spy_game_solution(nums):
    code=[0,0,7,'x']
        #[0,7,'x']
        #[7,'x']
        #['x'] lenght==1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1


print(spy_game_solution([1,2,4,0,0,7,5]))
print(spy_game_solution([1,0,2,4,0,5,7]))
print(spy_game_solution([1,7,2,0,4,5,0]))



#COUNT PRIMES:
#Write a function that returns the number of prime numbers that exist up to and including a given number


def count_primes(nums):
    lower=2
    upper=nums
    count=0
    for num in range(lower, upper + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               count+=1
    return count

print(count_primes(100))

#Solution

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)














