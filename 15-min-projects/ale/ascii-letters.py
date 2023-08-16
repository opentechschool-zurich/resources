# https://stackoverflow.com/questions/48451228/how-to-spread-a-python-array

letters = {}

c3 = [' ', 3 * '*', ' ']
lr = ['*', 3 * ' ', '*']
fl = [5 * '*']

# a = [[' ', 3 * '*', ' '], ['*', 3 * ' ', '*'], ['*', 3 * ' ', '*'], [5 * '*'], ['*', 3 * ' ', '*'], ['*', 3 * ' ', '*'], ['*', 3 * ' ', '*']]
# a = [c3, lr, lr, fl, lr, lr, lr]
# a = [[' ', 3 * '*', ' '], 2 * [['*', 3 * ' ', '*']]]
letters['a'] = [c3, *2 * [lr], fl, *3 * [lr]]
# print(a)

# z = 2 * [1, 2]
# print(z)

l4 = [4 * '*', ' ']
# b = [l4, lr, lr, l4, lr, lr, l4]
letters['b'] = [l4, *2 * [lr], l4, *2 * [lr], l4]

for letter, lines in letters.items():
	for line in lines:
		print(''.join(line))

#   *** 
#  *   *
#  *   *
#  *****
#  *   *
#  *   *
#  *   *

#  **** 
#  *   *
#  *   *
#  **** 
#  *   *
#  *   *
#  **** 
