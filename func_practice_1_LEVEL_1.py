#WARM-UPs

#LESSER OF TWO EVENS:
#Write a function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd

def myfunc(a,b):
    if a%2==0 and b%2==0:
        mylist=[a,b]
        return min(mylist)
    else:
        mylist=[a,b]
        return max(mylist)


print(myfunc(2,4))
print(myfunc(2,5))

#ANIMAL CRACKERS:
#Write a function takes a two-word string
#and returns True if both words begin with same letter

def myfunc2(text):
    mylist=(text.split(' '))
    if mylist[0][0] == mylist[1][0]:
        return True
    else:
        return False


print(myfunc2('Levelheaded Llama'))
print(myfunc2('Crazy Kangaroo'))

#MAKES TWENTY:
#Given two integers, return True if the sum of the integers is 20 or
#if one of the integers is 20. If not, return False

def myfunc3(a,b):
    if a + b == 20 or a==20 or b==20:
        return True
    else:
        return False

print(myfunc3(20,10))
print(myfunc3(12,8))
print(myfunc3(2,3))

# LEVEL 1

#OLD MACDONALD:
#Write a function that capitalizes the first and fourth letters of a name

def mc_don (name):
    namelist=list(name.capitalize())
    namelist[3]=namelist[3].capitalize()
    return ''.join(namelist)

print(mc_don('macdonald'))


#MASTER YODA:
#Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    yoda_list=sentence.split()
    return ' '.join(yoda_list[::-1])

print(master_yoda('I am home'))
print(master_yoda('We are ready'))


#ALMOST THERE:
#Given an integer n, return True if n is within 10 of either 100 or 200


def almost(num):
    if abs(num-100)<=10 or abs(num-200)<=10:
        return True
    else:
        return False

print(almost(90))
print(almost(104))
print(almost(150))
print(almost(209))















