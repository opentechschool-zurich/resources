#!/usr/bin/env python3

sentence = 'i am tired'
keyword = 'summer'
result = ''
odd = ''

for c in sentence:
    if odd != '':
        result += c + odd
        odd ='' 
    elif not c in keyword:
        result += c
    else:
        pos = keyword.find(c) + 1
        if pos > 0 and pos % 2 == 0:
            odd = c
if odd != '':
    result += odd
print(result)
