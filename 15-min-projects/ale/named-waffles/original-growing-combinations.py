# tries combination of growing size and, at each step, stops as soon as it finds
# one combination that can be fully served.
# there is a huge number of small combinations with a small number of items, but
# the algorithm will not have a hard time finding one that fulfills the condition.
# there are fewer bigger combination, but it's more likely that it will need to check
# many combination which fulfills the condition.
# we can stop when for a specific size there was no match.
import itertools

programmers = [p.lower() for p in ['Dennis', 'Aaron', 'Donald', 'Tim', 'Bjarne', 'Linus', 'Guido', 'James', 'Richard', 'Brian', 'Grace', 'Alan', 'Niklaus', 'Guy', 'Fabrice', 'Donald', 'Ken', 'John', 'Eric', 'Anders', 'Alexander', 'Charles', 'Alan', 'Ronald', 'Andrew', 'Leslie', 'Edsger', 'John', 'Keith', 'Barbara']]

def get_number_of_waffles(combination):
    waffle_counter = 0
    letters_used = {}
    for programmer in combination:
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

for i in range(1, len(programmers)):
    print(i)
    for combination in itertools.combinations(programmers, i):
        if get_number_of_waffles(combination) == i:
            print(combination)
            break;
    else:
        break
