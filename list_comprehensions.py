mystring="hello"

mylist=[]

for letter in mystring:
    mylist.append(letter)

print(mylist)


#list comprehension

mylist2=[letter for letter in mystring]

print(mylist2)

mylist3=[num for num in range(0,11,2)]
print(mylist3)

mylist4 = [num**2 for num in range(0,11)]

print(mylist4)

mylist5=[num**2 for num in range(0,11) if num%2==0]

print(mylist5)


#two same for loops 
celcius=[0,10,1,20,34.5]

fahrenheit=[(9/5*temp+32) for temp in celcius]

print(fahrenheit)

fah=[]
for temp in celcius:
    fah.append((9/5)*temp+32)
print(fah)

