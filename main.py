import random

game = ['R','P','S']
userOpt = 'R'
compOpt = 'R'

while (userOpt == compOpt):
    print('-----------------------------')
    print ()
    print('Rock-Paper-Scissors')
    print ()
    print('Use the following input methods for selection')
    print('input R for Rock')
    print('input P for Paper')
    print('input S for Scissors')
    print('-----------------------------')
    print()

    userOpt = input('pick a game option: ')
    userOpt = userOpt.upper()
    
    if userOpt in game:

        compOpt = random.choice(game)
        
        if (compOpt=='R' and userOpt=='S'):
            print("Computer Wins")

        elif (compOpt=='P' and userOpt=='R'):
            print ("Computer Wins")

        elif (compOpt=='S' and userOpt=='P'):
            print("Computer Wins")
            
        elif (compOpt == userOpt):
            print("TIE")

        else:
            print("You Win")
            
    else:
        userOpt = 'R'
        print()
        print('-----------------------------')
        print ("Invalid Input")
        print ("Pick a Valid Selection")
        
else:
    print ("Thank you for playing")
