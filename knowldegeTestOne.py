#Write a brief description of all the following Object Types and Data Structures we've learned about:
#For the full answers, review the Jupyter notebook introductions of each topic!

Numbers ="Numbers can be whole integers or floating, they are expressed without quotes"

Strings ="Any value expressed in quotes, even numbers"

Lists ="list is a combination of values like numbers or strings in [], is mutable, can be ordered,, sliced and have dubs"
 
Tuples ="are expressed in () imutable, can be orderd, sliced and have dubs"

Dictionaries="expressed in {} and is has a key value pairs unordeed until version 3.7"


#Numbers
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
#Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

Question2 = (2+2+1)*2*10+1-0.75
print("Question 2 is:", Question2)
#Answer these 3 questions without typing code. Then type code to check your answer.

#What is the value of the expression 4 * (6 + 5) = 44
a1=4 * (6 + 5)
#What is the value of the expression 4 * 6 + 5 = 29
a2=4 * 6 + 5
#What is the value of the expression 4 + 6 * 5 = 34
a3=4 + 6 * 5

print("Question 3:", a1,a2, a3)


#What is the type of the result of the expression 3 + 1.5 + 4? float

print("Question 3:", type(3 + 1.5 + 4))

#What would you use to find a number’s square root, as well as its square?
#To find a sq root of a number I can divide the number by 
#To get the square of a number I would mutiply by itself
print("Question 3:","Square Root of 16 =",16**0.5, "Square of 4 =", 4**2)

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
print("Question 4:")
print("Print out 'e'in " + s + " using indexing:", s[1])
# Reverse the string using slicing
print("Reverse the string " + s + " using slicing:", s[::-1])
print("Given the string hello, give two methods of producing the letter 'o' using indexing.")
# Print out the 'o'
# Method 1:
print("Method 1:", s[4])
# Method 2:
print("Method 2:", s[-1])

# Build this list [0,0,0] two separate ways.
print('Question 5: Build this list [0,0,0] two separate ways.')
L1=[0,0,0]
print('Method 1:', L1 )
L2= [0]*3
print('Method 2:', L2 )

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2]="Goodbye"

print("Question 6:",list3 )
#Sort the list below:
list4 = [5,3,4,6,1]
print("Sort the list: [5,3,4,6,1]", sorted(list4))


#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d2 = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d2['k1']['k2'])

# Getting a little tricker
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print(d3['k1'][0]['nest_key'][1][0])
# This will be hard and annoying!
d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d4['k1'][2]['k2'][1]['tough'][2][0])

print("Can you sort a dictionary? Why or why not?\nAnswer: No! Because normal dictionaries are mappings not a sequence.")
print("What is the major difference between tuples and lists?\nAnswer: Tuples are immutable")

print("How do you create a tuple?")
tu=(1,2,3)
print("Tuple:", tu)

print("What is unique about a set?\nSet has only unique values")

print("Use a set to find the unique values of the list: [1,2,2,33,4,4,11,22,3,3,2]")
list5 = [1,2,2,33,4,4,11,22,3,3,2]
setlist=set(list5)
print(setlist)

print("For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.")

# Answer before running cell False
print(2 > 3)
# Answer before running cell False
print(3 <= 2)
# Answer before running cell False
print(3 == 2.0)
# Answer before running cell True
print(3.0 == 3)
# Answer before running cell False
print(4**0.5 != 2)

print("Final Question: What is the boolean output of the cell block below?")
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False? False
print(l_one[2][0] >= l_two[2]['k1'] )
