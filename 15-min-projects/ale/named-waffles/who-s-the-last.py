programmers = ['Dennis', 'Aaron', 'Donald', 'Tim', 'Bjarne', 'Linus', 'Guido', 'James', 'Richard', 'Brian', 'Grace', 'Alan', 'Niklaus', 'Guy', 'Fabrice', 'Donald', 'Ken', 'John', 'Eric', 'Anders', 'Alexander', 'Charles', 'Alan', 'Ronald', 'Andrew', 'Leslie', 'Edsger', 'John', 'Keith', 'Barbara']

# 6 times the alphabet

def count_programmers():
    letters = {}
    counter = 0

    for name in programmers:
        for c in name.lower():
            if c in letters:
                if letters[c] == 6:
                    return counter
                else:
                    letters[c] += 1
            else:
                letters[c] = 1
        counter += 1

print(count_programmers())
