programmers = ['Dennis', 'Aaron', 'Donald', 'Tim', 'Bjarne', 'Linus', 'Guido', 'James', 'Richard', 'Brian', 'Grace', 'Alan', 'Niklaus', 'Guy', 'Fabrice', 'Donald', 'Ken', 'John', 'Eric', 'Anders', 'Alexander', 'Charles', 'Alan', 'Ronald', 'Andrew', 'Leslie', 'Edsger', 'John', 'Keith', 'Barbara']

# 6 times the alphabet

def count_programmers():
    letters = {}
    stuffed = []

    for name in programmers:
        processed = ""
        for c in name.lower():
            if c in letters:
                if letters[c] == 6:
                    for p in processed:
                        letters[p] -= 1
                    break
                else:
                    processed += c
                    letters[c] += 1
            else:
                letters[c] = 1
        else:
            stuffed.append(name)
    print(stuffed)
    return len(stuffed)

print(count_programmers())
