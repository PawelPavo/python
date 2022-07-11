import re


text="The agent's phone number is 408-555-1234. Call soon!"

print("phone" in text)

# Returns Match object - Returns only the first match
pattern="phone"
print(re.search(pattern,text))

# return None
pattern="Not in text"
print(re.search(pattern,text))


pattern="phone"
match=re.search(pattern,text)

# gets index location
print(match.span())
print(match.start())
print(match.end())

# Returns all matches

text2="my phone once, my phone twice"
print(re.findall('phone', text2))

# Returns the match object
for match in re.finditer('phone',text2):
    print(match)
    print(match.group())
