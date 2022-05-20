def myfunc2(word):
    mylist=[]
    mystring=""
    for char in list(word):
        if word.index(char)%2==0:
            mylist.append(char.upper())
        else:
            mylist.append(char)
    for char in mylist:
        mystring+=char
    return mystring


def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

print(myfunc('Geeksforgeks'))
