# scissor - rock -paper

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

# Instead of comparing each move by text, we can build the list of winning moves for the human

human_wins = [2, 0, 1] # for 0..2 values of human, computer values that make the human win
# computer_i = random.randint(0, 2) # if we go for the index, no need to set the computer move as a string
computer_i = moves.index(computer_move)
human_i = moves.index(human_move)
print(computer_i, human_i)
if human_i == computer_i:
    print('draw')
elif human_wins[human_i] == computer_i:
    print('human wins')
else:
    print('computer wins')

# Or, for readability, use a dict...

human_move_wins = {'scissor': 'paper', 'rock': 'scissor', 'paper': 'rock'}
if human_move == computer_move:
    print('draw')
elif human_move_wins[human_move] == computer_move:
    print('human wins')
else:
    print('computer wins')
