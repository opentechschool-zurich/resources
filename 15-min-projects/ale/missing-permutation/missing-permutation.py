#  Find the missing permutation:
#  https://rosettacode.org/wiki/Find_the_missing_permutation

import itertools

abcd = [
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

# solution with itertools
abcd_set = set(abcd)
all_abcd_set = set(''.join(item) for item in itertools.permutations(['A', 'B', 'C', 'D']))
print(all_abcd_set.difference(abcd_set))

# solution without itertools
solution = ''
for i in range(4):
    abcd_dic = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
    }
 
    for item in abcd:
        abcd_dic[item[i]] += 1

    solution += min(abcd_dic, key=abcd_dic.get)
print(solution)
