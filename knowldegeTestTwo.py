#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
st2=st.split(' ')
for word in st2:
    if word[0] =='s':
        print(word)
        

#Use range() to print all the even numbers from 0 to 10.

for num in range(0,11):
    if num%2 == 0:
        print(num)

print(f'Range: {list(range(0,11,2))}')

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

for num in range(1,51):
    if num%3 == 0:
        print(num)

myRange = [num for num in range(1,51) if num%3 ==0]
print(myRange)


#Go through the string below and if the length of a word is even print "even!"
        
st3 = 'Print every word in this sentence that has an even number of letters'


for word in st3.split(' '):
    if len(word)%2==0:
        print(f'{word} has {len(word)} chars in it, so its even')
    else:
        print(f'{word} has {len(word)} chars in it, so its odd')

#Write a program that prints the integers from 1 to 100.
#But for multiples of three print "Fizz" instead of the number,
#and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".


for num in  range(0,101):
    if(num%15==0):
        print('FizzBuzz')
    elif(num%5==0):
        print('Buzz')
    elif(num%3)==0:
        print('Fizz')
    else:
        print(num)

#Use List Comprehension to create a list of the first letters of every word in the string below:

st4 = 'Create a list of the first letters of every word in this string'
list_st4=st4.split(' ')

for word in st4.split(' '):
    print(word[0])


print([word[0] for word in st4.split(' ')])

