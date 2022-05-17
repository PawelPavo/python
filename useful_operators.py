#range - all the way up to but not including
#range (start, stop, step) stop is not included


for num in range(0,11,2):
    print(num)

#range is a generator which you need to cast the list to get the numbers
print(list(range(0,11,2)))

#inumerate

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1


#enumerate manual

index_count2 = 0

word = 'abcde'

for letter in word:
    print(word[index_count2])
    index_count2 += 1

# this returnds tuples of index and letter pairs
for letter in enumerate(word):
    print(letter)

#this is from pervious how to break the tuple
for index, letter in enumerate(word):
    print(index)
    print(letter)

#zip
#zip will ignore the chars if one list is longer, so if there are extra
#chars in list, it will only form tuples of the shortest list

mylist1=[1,2,3]
mylist2=['a','b','c']
mylist3=[100,200,300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1,mylist2,mylist3)))


#bool - works in strings, dictionaries etc.
print('x' in [1,2,3])

print('x' in ['x','y','z'])
