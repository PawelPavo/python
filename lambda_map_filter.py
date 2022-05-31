#map function

def square(num):
    return num**2

my_nums=[1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names=['Andy','Pawel','Paul','Sally','Eve']

print(list(map(splicer,names)))



#filter function - filters T or F

def check_even(num):
    return num%2==0

my_numbs=[1,2,3,4,5,6]

for n in filter(check_even, my_numbs):
    print(n)

print(list(filter(check_even, my_numbs)))


#lambda expressions - its an anonymous function(you dont name them) use word lambda

def square2(num):
    result=num**2
    return result

print(square2(3))

#transorming above function to lambda expression

#Step 1
def square3(num):
    return num**2

#step 2
def square4(num): return num**2


#step 3
square5 = lambda num: num**2
print(square(5))

#examples
my_numbs2=[1,2,3,4,5,6]

print(list(map(lambda num: num**2, my_numbs2)))

print(list(filter(lambda num:num%2==0, my_numbs2)))

#names list is defined above
print(list(map(lambda n:n[0],names)))
print(list(map(lambda n:n[::-1],names)))



