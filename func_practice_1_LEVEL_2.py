#FIND 33:
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33 (some_list):
    for i in range(0,len(some_list)):
        if some_list[i]==3:
            if some_list[i]==some_list[i+1]:
                return True
            else:
                return False

print(has_33([1, 3, 3]))

print(has_33([1, 3, 1, 3]))

print(has_33([3, 1, 3]))

#Solution
def has_33_solution(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

print(has_33_solution([1, 3, 3]))
print(has_33_solution([1, 3, 1, 3]))
print(has_33_solution([3, 1, 3]))


#PAPER DOLL:
#Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    my_list=[]
    for i in range(len(text)):
         my_list.append(text[i]*3)
    return ''.join(my_list)

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


#Solution
def paper_doll_solution(text):
    result=''
    for char in text:
        result+=char*3
    return result

print(paper_doll_solution('Hello'))
print(paper_doll_solution('Mississippi'))


#BLACKJACK:
#Given three integers between 1 and 11, if their sum is less than or equal to 21,return their sum.
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack (a,b,c):
    num_sum = a+b+c
    bust=0
    if a==11 or b==11 or c==11:
        bust=num_sum-10
        return bust
    if num_sum >21 or bust > 21:
            return 'BUST'
    if num_sum <= 21:
        return num_sum

print(blackjack(5,6,7))
print(blackjack(9,9,9) )
print(blackjack(9,9,11))

#Solution
def blackjack_solution(a,b,c):
    if sum([a,b,c])<= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return 'BUST'


print(blackjack_solution(5,6,7))
print(blackjack_solution(9,9,9) )
print(blackjack_solution(9,9,11))

print('NEXT QUESTION')

#SUMMER OF '69:
#Return the sum of the numbers in the array,
#except ignore sections of numbers starting with a 6 and extending to the next 9
#(every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(nums):
    my_list=[]
    for i in nums:
        if i in range(6,10):
            continue
        else:
            my_list.append(i)
    return(sum(my_list))
        
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9])) 
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([2, 1, 6, 8, 9, 11]))


#solution

def summer_69_solution(arr):
    total=0
    add=True
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False
        while not add:
            if num !=9:
                break
            else:
                add=True
                break
    return total

print(summer_69_solution([1, 3, 5]))
print(summer_69_solution([4, 5, 6, 7, 8, 9])) 
print(summer_69_solution([2, 1, 6, 9, 11]))
print(summer_69_solution([2, 1, 6, 8, 9, 11]))



