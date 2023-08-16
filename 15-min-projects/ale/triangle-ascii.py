"""
3
  x
 x x
x x x -> 5
  3
5
    x
   x x
  x   x
 x     x
x x x x x -> 9
    5
7
      x
     x x
    x   x
   x     x
  x       x
 x         x
x x x x x x x -> 13
      7
"""

def draw(n):
    if n < 3:
        return
    triangle = []
    for i in range(n - 1):
        line = " " * (n - i - 1) + '#'
        if i > 0:
            line += (i * 2 - 1) * ' ' + '#'
        triangle.append(line)
    triangle.append((n * '# ').strip())
    for line in triangle:
        print(line)

draw(10)
