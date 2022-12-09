# 12/09
# 문제를 너무 어렵게 생각했나봐..

def nextlevel(a):
    if a % 2 == 0:
        return a // 2
    else:
        return a // 2 + 1


def solution(n, a, b):
    count = 1
    while (True):
        a = nextlevel(a)
        b = nextlevel(b)
        if a == b:
            break
        count += 1
    return count


print(solution(8, 17, 32))
