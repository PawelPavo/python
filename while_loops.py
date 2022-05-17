x=0

while x < 5:
    print(f'The current value of x is {x}')
    #x = x+1
    #or you can increment like this:
    x+=1
else:
    print('X is not less then 5')


#pass

y=[1,2,3]

#placing pass here without any directive will prevent error saying
#that you need to have something here
#its for holding function if its not finished yet

for i in y:
    pass
print('end of pass')

#continue
# continue means that if the condition is met like 'a' == 'a', don't print but
#go back to the most enclosing loop and go to throug again
#in the next order seqance so it SKIPS that print and goes to the next
mystring="Sammy"
for letter in mystring:
    if letter =='a':
        continue
    print(letter)
print('end of coninue')


#break
#this breaks the loop at the condition given

mystring2="Sammy"
for letter in mystring:
    if letter =='a':
        break
    print(letter)

z=0
while z < 5:
    if z == 2:
        break
    print(z)
    z += 1
    
print('end of break')
