letters = {}

c = [2 * ' ', '*', 2 * ' ']
c3 = [' ', 3 * '*', ' ']
l = ['*', 4 * ' ']
r = [4 * ' ', '*']
lr = ['*', 3 * ' ', '*']
fl = [5 * '*']
l4 = [4 * '*', ' ']

letters['a'] = [c3, *2 * [lr], fl, *3 * [lr]]
letters['b'] = [l4, *2 * [lr], l4, *2 * [lr], l4]
letters['c'] = [c3, lr, *3 * [l], lr, c3]
letters['d'] = [l4, *5 * [lr], l4]
letters['e'] = [fl, *2 * [l], l4, *2 * [l], fl]
letters['f'] = [fl, *2 * [l], l4, *3 * [l]]
letters['g'] = [c3, lr, l, ['*  **'], *2 * [lr], c3]
letters['h'] = [*3 *[lr], fl, *3 *[lr]]
letters['i'] = [fl, *5 * [c], fl]
letters['j'] = [fl, *4 * ['   * '], ['*  * '], [' **  ']]
letters['k'] = [lr, ['*  * '], ['* *  '], ['**   '], ['* *  '], ['*  * '], lr]
letters['l'] = [*6 * [l], fl]
letters['m'] = [*2 *[lr], ['** **'], ['* * *'], *3 *[lr]]
letters['n'] = [*2 *[lr], ['**  *'], ['* * *'], ['*  **'], *2 *[lr]]
letters['o'] = [c3, *5 * [lr], c3]
letters['p'] = [l4, *2 * [lr], l4, *3 * [l]]
letters['q'] = [c3, *3 * [lr], ['* * *'], ['*  * '], [' ** *']]
letters['r'] = [l4, *2 * [lr], l4, ['* *  '], ['*  * '], lr]
letters['s'] = [c3, lr, l, c3, r, lr, c3]
letters['t'] = [fl, *6 * [c]]
letters['u'] = [*6 * [lr], c3]
letters['v'] = [*5 * [lr], ' * * ' , c]
letters['w'] = [*4 * [lr], *2 * ['* * *'] , [' * * ']]
letters['x'] = [*2 * [lr], [' * * '], c, [' * * '], *2 * [lr]]
letters['y'] = [*2 * [lr], [' * * '], *3 * [c]]
letters['z'] = [fl, r, ['   * '], ['  *  '], [' *   '], l, fl]



for letter, lines in letters.items():
	for line in lines:
		print(''.join(line))

def display(word, letters):
    for i in range(7):
        for c in word:
            print(''.join(letters[c][i]), end = ' ')
        print()

display('chaos', letters)
