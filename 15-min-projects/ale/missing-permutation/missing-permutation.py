#  Find the missing permutation:
#  https://rosettacode.org/wiki/Find_the_missing_permutation

import itertools

permutations = [
     'ABCD',
     'CABD',
     'ACDB',
     'DACB',
     'BCDA',
     'ACBD',
     'ADCB',
     'CDAB',
     'DABC',
     'BCAD',
     'CADB',
     'CDBA',
     'CBAD',
     'ABDC',
     'ADBC',
     'BDCA',
     'DCBA',
     'BACD',
     'BADC',
     'BDAC',
     'CBDA',
     'DBCA',
     'DCAB',
]

all_permutations = [''.join(l) for l in itertools.permutations(['A', 'B', 'C', 'D'])]

# 1. solution with all permutations (itertools)
for p in all_permutations:
   if not p in permutations: 
        print(p)
        break;

# 2. solution with all permutations (itertools) and sets
abcd_set = set(permutations)
all_abcd_set = set(''.join(item) for item in itertools.permutations(['A', 'B', 'C', 'D']))
print(all_abcd_set.difference(abcd_set))

# 3. solutions with all permutations, but without in (double for loop)
for p in all_permutations:
    found = False
    for pp in permutations:
        if p == pp:
            found = True
            break
    if not found:
        print(p)
        break;

# 4. solution without all permutations
solution = ''
for i in range(4):
    abcd_dic = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
    }
 
    for item in permutations:
        abcd_dic[item[i]] += 1

    solution += min(abcd_dic, key=abcd_dic.get)
print(solution)



