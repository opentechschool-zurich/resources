from random import shuffle

from random import shuffle

programmers = ['Dennis', 'Aaron', 'Donald', 'Tim', 'Bjarne', 'Linus', 'Guido', 'James', 'Richard', 'Brian', 'Grace', 'Alan', 'Niklaus', 'Guy', 'Fabrice', 'Donald', 'Ken', 'John', 'Eric', 'Anders', 'Alexander', 'Charles', 'Alan', 'Ronald', 'Andrew', 'Leslie', 'Edsger', 'John', 'Keith', 'Barbara']


def get_number_of_waffles(permutation):
    waffle_counter = 0
    letters_used = {}
    for programmer in permutation:
        for letter in programmer:
            if letter in letters_used:
                if letters_used[letter] == 6:
                    return waffle_counter
                letters_used[letter] += 1
            else:
                letters_used[letter] = 1
        waffle_counter += 1

    # it should never get here...
    return waffle_counter

best_queue = []
max_waffles = 0

# itertools.permutations() creates an iterator and not a list:
# trying to create a list would probably use all the RAM available in the whole world...
# (you're welcome to check if this is true or not...)
while True:
    shuffle(programmers)
    waffles_number = get_number_of_waffles(programmers)
    if waffles_number > max_waffles:
        best_queue = programmers
        max_waffles = waffles_number
        print(max_waffles, best_queue)

