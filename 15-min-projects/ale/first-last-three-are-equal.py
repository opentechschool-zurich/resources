# Find words whose first and last three letters are equal
# Variants:
# - Count the number of matching words
# - Use a "palindrom" camparison (ion....noi)
import urllib.request

url = 'https://web.archive.org/web/20180611003215if_/http://www.puzzlers.org:80/pub/wordlists/unixdict.txt'

# i = 0
# for line in urllib.request.urlopen(url):
#     print(line.decode('utf-8').strip())
#     i += 1
#     if i > 20:
#         break

# ionisation


# words = ['abcdef', 'ionisation', 'thatsnot', 'oko']
# for word in words:
#     if len(word) >= 3:
#         # if word[0] == word[-3] and word[1] == word[-2] and word[2] == word[-1]:
#         # word.substring(0,3) == word.sustring(world.length - 3, world.length)
#         if word[0:3] == word[-3:]:
#             print(word)
#             break


for line in urllib.request.urlopen(url):
    word = line.decode('utf-8').strip()
    if len(word) >= 6:
        if word[0:3] == word[-3:]:
            print(word)
            break
