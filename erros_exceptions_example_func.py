def ask_for_int():
    while True:
        try:
            result=int(input('Please provide number: '))
        except:
            print('Whoops, that is not a number')
            continue
        else:
            print('Yes, Thank you!')
            break
        finally:
            print('End of Try/Except/Finally')
            print('I will always run at the end')
ask_for_int()
