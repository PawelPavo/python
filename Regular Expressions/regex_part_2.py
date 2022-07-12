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
