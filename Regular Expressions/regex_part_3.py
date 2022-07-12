#https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20447375#questions

import re


text="My phone number is 408-555-1234"

phone=re.search('408-555-1234',text)
print(phone.group())

# we need to add 'r' so Python know its regex pattern
# if we change the phone number this method will still find it
phone_2=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone_2.group())


# QUANTIFIERS
phone_3=re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone_3.group())


# Getting area code - COMPILE FUNCTION
# This function groups patterns by using () around them

phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results=re.search(phone_pattern,text)

print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))

# Additional Reges Syntax

# OR operator is: pipe |
sample1=re.search(r'cat | dog','The dog is here')
print(sample1)


# Wild Card
# the '.' is the wild card character

sample2=re.findall(r'...at', 'The cat in the hat went splat there')
print(sample2)

# Starts With and End With
# starts with is represented by "^"
# This works only for the entire sentence
# so if sentece doesnt start with a number it wont work ex. "The 2 is a number"

sample3=re.findall(r'^\d','1 is a number')
print(sample3)


# End with is represented by "$"
sample4=re.findall(r'\d$','The number is 2')
print(sample4)


# EXCLUSIONS

phrase="there are 3 numbers 34 inside 5 this sentence"

pattern=r'[^\d]'
pattern2=r'[^\d]+'
print(re.findall(pattern,phrase))
print(re.findall(pattern2,phrase))

# Remove punctuations
test_phrase='This is a phrase! But is has punctuations. How can we remove it?'
# NOTE there is a space in the punctiation lists after ? to remove spaces as well
clean=re.findall(r'[^!.? ]+', test_phrase)

print(' '.join(clean))

# INCLUSIONS

phrase2='Only find the hypen-words in this sentence. But you do not know how long-ish they are'

pattern2=r'[\w]+-[\w]+'

print(re.findall(pattern2, phrase2))















