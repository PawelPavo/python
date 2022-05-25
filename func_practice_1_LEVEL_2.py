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
