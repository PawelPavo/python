
#just for fun, not a real problem :)
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#print_big('a')

#out:   *  
#      * *
#     *****
#     *   *
#     *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".



def print_big(letter):
    patterns={1:'  *  ', 2:' * * ',3:' *** ', 4:'*   *',5:'*****',6:'*',7:'* * *', 8:'** **'}
    text={'A':[1,2,5,4,4],'B':[5,4,5,4,5],'P':[5,4,5,6,6], 'W':[4,4,7,8,4],'E':[5,6,5,6,5], 'L':[6,6,6,6,5]}
    for pattern in text[letter.upper()]:
        print(patterns[pattern])


print()
print_big('p')
print()
print_big('a')
print()
print_big('w')
print()
print_big('e')
print()
print_big('l')
print()
