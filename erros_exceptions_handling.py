def add(n1,n2):
    print(n1+n2)

add(10,20)


try:
    # ATTEMPT THIS CODE
    # MAY HAVE AN ERROR

    result = 10 + 10 # Change to string to force error

except:
    print('It looks like you are not adding correctly!')

else:
    print("ALL went well")
    print(result)
