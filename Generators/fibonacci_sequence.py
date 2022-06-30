# Creating a fibamacci sequance generator

def gen_fibon(n):
    a=1
    b=1
    for i in range(n):
        yield a
        
        # tuple matching
        a,b = b,a+b
        '''
        temp=a
        a=b
        b=temp+b
        '''
for number in gen_fibon(10):
    print(number)

print('========== BREAK ==========')

# if this was a non-generator function
# way less memory efficiant because everything is held in memory in a list
# and not yielded as we needed

def gen_fibon_2(n):
    a=1
    b=1
    output=[]
    for i in range(n):
        output.append(a)
        #a,b = b,a+b
        temp=a
        a=b
        b=temp+b
    return output

for number in gen_fibon_2(10):
    print(number)

