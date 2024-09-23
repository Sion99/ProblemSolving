def find_alphabet(c, ducks):
    for i in range(len(ducks)):
        if c == ducks[i][-1]:
            return i
    return -1


quack = input()

ducks = []



for c in quack:
    if c == 'q':
        idx = find_alphabet('k', ducks)
        if idx == -1:
            ducks.append('q')
        else:
            ducks[idx] += 'q'
    elif c == 'u':
        idx = find_alphabet('q', ducks)
        if idx == -1:
            print(-1)
            exit()
        else:
            ducks[idx] += 'u'
    elif c == 'a':
        idx = find_alphabet('u', ducks)
        if idx == -1:
            print(-1)
            exit()
        else:
            ducks[idx] += 'a'
    elif c == 'c':
        idx = find_alphabet('a', ducks)
        if idx == -1:
            print(-1)
            exit()
        else:
            ducks[idx] += 'c'
    else:
        idx = find_alphabet('c', ducks)
        if idx == -1:
            print(-1)
            exit()
        else:
            ducks[idx] += 'k'

for duck in ducks:
    if len(duck) % 5 != 0:
        print(-1)
        exit()
print(len(ducks))