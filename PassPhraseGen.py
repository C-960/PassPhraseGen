import random
import os

specialChars = '&%$!?@#'

fVerbs = None
fAdjective = None
fNouns = None

vTotal = 0
aTotal = 0
nTotal = 0

try:
    fVerbs = open('verbs.txt')
    fAdjectives = open('adjectives.txt')
    fNouns = open('nouns.txt')

    vTotal = sum(1 for line in open('verbs.txt')) 
    aTotal = sum(1 for line in open('adjectives.txt')) 
    nTotal = sum(1 for line in open('nouns.txt')) 

except Exception as e:
    print('One or more word files could not be opened')
    print(e)


v = random.randint(1, vTotal)
a = random.randint(1, aTotal)
n = random.randint(1, nTotal)

password = ''

for i, word in enumerate(fVerbs):
    if i == v:
        password = word.rstrip().title()
    elif i > v:
        break

for i, word in enumerate(fAdjectives):
    if i == a:
        password = password + word.rstrip().title()
    elif i > a:
        break

for i, word in enumerate(fNouns):
    if i == n:
        password = password + word.rstrip().title()
    elif i > n:
        break

password = password + random.choice(specialChars)
print('\nTotal possibilities with current wordlists and special characters:')
print('{:,}'.format(vTotal * aTotal * nTotal * len(specialChars)))
print('\nPassword: ', password, '\n')
