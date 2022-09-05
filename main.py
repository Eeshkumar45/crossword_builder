# included direction successfully
# rewrite setting coordinates so that no intersections happen
import random
import numpy
import time
type = 0
lenoflargesword = 0
size = 0
#kkqw = time.t

'''
white = '\u001b[30m'
yellow = '\u001b[32m'
cyan = '\u001b[36m' '''
#colors = ['\033[92m','\033[93m','\033[91m','\033[1m','\033[4m']
#         yellow     darkyellow   pale red
basic = '\u001b[30m'
yellow = '\u001b[32m'
cyan = '\u001b[36m'
basic=''
yellow=''
cyan=''
# prints the word letter by letter ex:- hello -- h  e  l  l  o(used when dxn is horizontal)
def p(f):
    for i in range(len(f)):
        print(yellow+f[i].upper(), end='  ')
skip = 0

def prin():
    global skip
    for i in range(0,size):
        for j in range(0,size):
            foundcos = 0
            if skip > 0:
                skip -= 1
                continue
            for c in range(0, noofwords):
                if coordinates[c][0] == i and coordinates[c][1] == j:
                    if i == 0 and j == 0:
                        continue
                    if elementsprinted[c] == len(words[c]):
                        continue
                    foundcos = 1
                    if dxn[c] == 0:
                        p(words[c])
                        skip = len(words[c]) - 1
                    elif dxn[c] == 1:
                        print(cyan + words[c][elementsprinted[c]].upper(), end='  ' + basic)
                        elementsprinted[c] += 1
                        coordinates[c][0] += 1
            if foundcos == 0:
                print(basic +'X', end='  ' + basic)
        print('')

allletters = 'abcdefghijklmnopqrstuvwxyz'
while(type not in [1,2]):
    type = int(input('1-- manual\n2-- automated : '))


print('number of words :', end=' ')


noofwords = int(input(''))

words = []


# input words and setting length of largest word simultaneously

for i in range(noofwords):
    print('[{}] enter word :'.format(i + 1), end='  ')
    words.append(input(''))
    if len(words[i]) > lenoflargesword:
        lenoflargesword = len(words[i])

if type == 1:
    size = int(input('size of matrix(nxn) (recomended : {}) :'.format(3*lenoflargesword)))
elif type == 2:
    size = 3 * lenoflargesword

elementsprinted = numpy.full(noofwords, 0)
coordinates = numpy.empty((noofwords,2))

# change this lines
# giving random coordinates for the words
dxn = numpy.full(noofwords, 0)
if type == 2:
    coordinates = numpy.full(noofwords * 2, 0)
    for i in range(0, noofwords * 2):
        coordinates[i] = random.randint(0, size - lenoflargesword)

    # giving ranoom dxn for words(0-horizontal and 1- vertical)
    ''' todo - use two more dxn 3 -- cross_down_right 4 -- cross_down_left
    (use the same modes to for writing up(reverse the word))'''
    for i in range(noofwords):
        dxn[i] = random.randint(0, 1)
if type == 1:
    for i in range(0,noofwords):
        coordinates[i][0] = int(input('give valid coordinate_X for word {} : '.format(words[i])))
        coordinates[i][1] = int(input('give valid coordinate_Y for word {} : '.format(words[i])))
        dxn[i] = int(input('dxn :\n1--vertical\n0--horizontal :'))
        coordinates = coordinates.reshape(noofwords,2)

        prin()
        for j in range(0,noofwords):
            if dxn[j] == 1:
                coordinates[j][0] -= len(words[j])
        elementsprinted = numpy.full(noofwords, 0)

coordinates = coordinates.reshape(noofwords, 2)

foundcos = 0

print(dxn)
print(coordinates)

## printing the matrix
for i in range(0, size):
    for j in range(0, size):
        foundcos = 0
        if skip > 0:
            skip -= 1
            continue
        for c in range(0, noofwords):
            if coordinates[c][0] == i and coordinates[c][1] == j:
                if elementsprinted[c] == len(words[c]):
                    continue
                foundcos = 1
                if dxn[c] == 0:
                    p(words[c])
                    skip = len(words[c]) - 1
                elif dxn[c] == 1:
                    print(cyan+ words[c][elementsprinted[c]].upper(), end='  '+basic)
                    elementsprinted[c] += 1
                    coordinates[c][0] += 1
        if foundcos == 0:
            print(basic+allletters[random.randint(0, 25)], end='  '+basic)
    print('')
