import timeit

#Running both functions 100,000 times to see which is faster

# FUNCTION 1
stmt_1= '''
func_one(100)
'''

setup_1= '''
def func_one(n):
    return [str(num) for num in range(n)]
'''


print(timeit.timeit(stmt_1,setup_1,number=100000))


# FUNCTION 2
stmt_2='''
func_two(100)
'''

setup_2='''
def func_two(n):
    return list(map(str,range(n)))
'''

print(timeit.timeit(stmt_2,setup_2,number=100000))

