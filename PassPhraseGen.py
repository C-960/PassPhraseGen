import random
import os

fVerbs = None
fAdjective = None
fNouns = None

v = 0
a = 0
n = 0

try:
    fVerbs = open('verbs.txt')
    fAdjectives = open('adjectives.txt')
    fNouns = open('nouns.txt')

    v = sum(1 for line in open('verbs.txt')) 
    a = sum(1 for line in open('adjectives.txt')) 
    n = sum(1 for line in open('nouns.txt')) 

except Exception as e:
    print('One or more word files could not be opened')
    print(e)

v = random.randint(1, v)
a = random.randint(1, a)
n = random.randint(1, n)

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
specialChars = '&%$!?'
password = password + random.choice(specialChars)
print(password)
