
def myfunc (a,b,c=0,d=0,e=0):
    #returns 5% of the sum of a and b
    return sum((a,b,c,d,e))*0.05

print(myfunc(40,60))
print(myfunc(40,60,100))
print(myfunc(40,60,30,500))



#Using *args to pass as many args as we want
#we dont need to use the word args, the * is what matters but use args as convestion

def myfunc2 (*args):
    #returns 5% of the sum of a and b
    return sum(args)*0.05

print(myfunc2(40,60))
print(myfunc2(40,60,100))
print(myfunc2(40,60,30,500))


def myfunc3 (*args):
    for item in args:
        print(item)

myfunc3(40,60)
myfunc3(40,60,100)
myfunc3(40,60,30,500)


#Using **kwargs

def myfunc4(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc4(fruit='apple', veggie='lettuce')


#using both *args and **kwargs

def myfunc5(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
          
myfunc5(10,20,30,fruit="apple", food="pizzas", animal="dog")


          

