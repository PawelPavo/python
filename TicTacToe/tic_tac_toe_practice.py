#Displaying information

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
row2[1]='X'

display(row1,row2,row3)

#Accepting user input

#position_index = int(input("Choose an index position: "))              
#row2[position_index]


# Validating user input

def user_choice():
    # VARIABLES
    
    # initial values
    choice ='WRONG'
    acceptable_range = range(0,10)
    within_range = False

    # TWO CONDITIONS TO CHECK - DIGIT or WITHIN_RANGE == False
    while choice.isdigit()==False or within_range==False:
        choice = input("Please enter a number (0-10): ")

        # DIGIT CHECK
        if choice.isdigit()==False: # this check is redundent, choice.isdigit() does't need to be == False
            print(f'Sorry, "{choice}" is not a digit!')
            
        # RANGE CHECK
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_ramge = False #this doesn't need re-assignment, but it's for show
                print('Sorry, you are out of acceptable 0 to 10 range!')
        
    return int(choice)

user_choice()
