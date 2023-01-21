answer = 0


def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag


def nqueen(i, col):
    global answer
    n = len(col) - 1
    if (promising(i, col)):
        if i == n:
            # print(col[1:n+1])
            answer += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                nqueen(i+1, col)


n = int(input())
col = [0] * (n+1)
nqueen(0, col)
print(answer)
