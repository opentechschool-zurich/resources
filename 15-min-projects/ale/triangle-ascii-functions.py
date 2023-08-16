def repeat(n, chars):
    return n * chars

def draw(n):
    if n < 3:
        return
    for i in range(n):
        line = repeat(n - i - 1, " ")  + '#'
        if i == n - 1:
            line += repeat(n - 1, ' #')
        elif i > 0:
            line += repeat(i * 2 - 1, ' ')  + '#'
        print(line)

draw(10)

