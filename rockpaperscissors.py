import random

computer_win = 0
user_win = 0
jugadas = 0

def play(computer_win, user_win, jugadas):
    while (jugadas < 3):
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower
        computer = random.choice(['r','p','s'])        
        if user == computer:
            jugadas = jugadas + 1
            print( f'It\'s a tie. Round {jugadas}/3')
        if is_win(user, computer):
            user_win +=1
            jugadas = jugadas + 1
            print( f'You won! Round {jugadas}/3')
        else:
            computer_win +=1
            jugadas = jugadas + 1
            print( f'You lost! Round {jugadas}/3')


    if computer_win >2 or user_win>2:        
        if computer_win > user_win:
            print("The computer won")
        elif user_win > computer_win:
            print( "You won!")
        else:
            print( "It's a tie jjjjj")
        
        

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player =='s' and opponent =='p') \
        or (player =='p' and opponent == 'r'):
        return True
    



play(computer_win,user_win,jugadas)