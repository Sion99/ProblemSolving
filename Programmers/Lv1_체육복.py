# 12/20
# 왤케 잘 안풀리지..

def solution(n, lost, reserve):
    answer = 0
    real = [1 for _ in range(n)]
    while (lost):
        temp = lost.pop()
        real[temp-1] -= 1
    while (reserve):
        temp = reserve.pop()
        real[temp-1] += 1
    print(real)
    for i in range(len(real)):
        if i == 0 and real[i] == 0:
            if real[i+1] == 2:
                real[i+1] -= 1
                real[i] += 1
        elif i < len(real)-1 and real[i] == 0:
            if real[i+1] == 2:
                real[i+1] -= 1
                real[i] += 1
        elif i == len(real)-1 and real[i] == 0:
            if real[i-1] == 2:
                real[i-1] -= 1
                real[i] += 1
    print(real)
    zeros = real.count(0)
    answer = n - zeros
    return answer
