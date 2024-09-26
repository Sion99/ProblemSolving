n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(m)]

state = []

for i in range(m):
    order = list(map(int, input().split()))
    if order[0] == 1:
        train[order[1] - 1][order[2] - 1] = 1
    elif order[0] == 2:
        train[order[1] - 1][order[2] - 1] = 0
    elif order[0] == 3:
        for j in range(19, 0, -1):
            train[order[1] - 1][j] = train[order[1] - 1][j - 1]
        train[order[1] - 1][0] = 0
    elif order[0] == 4:
        for j in range(19):
            train[order[1] - 1][j] = train[order[1] - 1][j + 1]
        train[order[1] - 1][0] = 0

for t in train:
    if t not in state:
        state.append(t)

print(len(state))