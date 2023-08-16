# pick a random item in a list, without using the random function

fruits = ['apple', 'pear', 'orange', 'lemon']

import time


fruits = ['apple', 'pear', 'orange', 'lemon']

def random_item(l):
    return l[ time.localtime().tm_sec % len(l) ]


print(random_item(fruits))
