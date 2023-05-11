i# scissor - rock -paper

import random


moves = ['scissor', 'rock', 'paper']

human_move = ""
while human_move not in moves:
    print('please write scissors, rock or paper')
    human_move = input('your move: ')

computer_move = random.choice(moves)
print('computer move: ' + computer_move)

if human_move == computer_move:
    print('it is a draw')
elif (human_move == 'rock' and computer_move == 'scissor' or
     human_move == 'paper' and computer_move == 'rock' or
     human_move == 'scissor' and computer_move == 'paper'):
     print('human wins')
else:
    print('computer wins')

