hi = [1,2,1,34,6,34,1,2,7,6,4,2,2,2,6,7]
bye= ['hello', 'hi', 'bye', 'yes', 'hi', 'hello']


def removeDupsWithSet(myList):
    newList=[]
    myListSet = (set(myList))
    for x in myListSet:
        newList.append(x)
    newList.sort()
    print(newList)

removeDupsWithSet(bye)
