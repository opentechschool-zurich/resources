# Okay, here is the issue: In about an hour, 30 famous open source programmers will be standing in line here for a waffle. I want to decorate special waffles for them with their names on them. The names shall be written with fine Belgian chocolate letters that I bought. I bought six sets of letters (each set has 26 letters of the English Alphabet). I probably won’t have enough letters to write all their names. In which order shall the programmers stand in line for me to be able to inscribe as many waffles as possible? Here are the programmers’ names":
# 
# Dennis, Aaron, Donald, Tim, Bjarne, Linus, Guido, James, Richard, Brian, Grace, Alan, Niklaus, Guy, Fabrice, Donald, Ken, John, Eric, Anders, Alexander, Charles, Alan, Ronald, Andrew, Leslie, Edsger, John, Keith, Barbara

import itertools

programmers = [p.lower() for p in ['Dennis', 'Aaron', 'Donald', 'Tim', 'Bjarne', 'Linus', 'Guido', 'James', 'Richard', 'Brian', 'Grace', 'Alan', 'Niklaus', 'Guy', 'Fabrice', 'Donald', 'Ken', 'John', 'Eric', 'Anders', 'Alexander', 'Charles', 'Alan', 'Ronald', 'Andrew', 'Leslie', 'Edsger', 'John', 'Keith', 'Barbara']]


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
for permutation in itertools.permutations(programmers):
    waffles_number = get_number_of_waffles(permutation)
    if waffles_number > max_waffles:
        best_queue = permutation
        max_waffles = waffles_number

print(max_waffles, best_queue)
