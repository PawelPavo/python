from random import shuffle

example = [1,2,3,4,5,6,7]

#You have to run this function to assing the shuffled list,
#because shuffle does it in place, so we need to run it, and assign it
#just like print needs a return to be assigned this needs a return to save a var with new shuffled list


# 3 CUP MONTE
def shuffle_list(random_list):
    shuffle(random_list)
    return random_list

def player_guess():
    player_input_guess=''
    while player_input_guess not in ['0','1','2']:
        player_input_guess = input("Pick a number: 0,1 or 2: ")
    return int(player_input_guess)

def check_guess(mylist, guess_from_func):
    if mylist[guess_from_func] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)


#initial list
mylist = [' ','O',' ']

#shuffle list
mix_list = shuffle_list(mylist)

#User guess
guess = player_guess()

#Check guess
check_guess(mix_list, guess)

