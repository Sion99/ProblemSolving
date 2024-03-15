import sys
from collections import deque


# 0 - 9999 십진수 저장 가능

# D: n값 2배, 9999 초과시 10000으로 나눈 나머지 값 -> 즉 해당 값에서 - 10000 한 값 (2n mod 10000)
# S: n - 1, n이 0인 경우 9999 (값이 음수인경우 9999)
# L: 각 자릿수 왼쪽으로 회전, 1 2 3 4 -> 2 3 4 1
# R: 각 자릿수 오른쪽으로 회전, 1 2 3 4 -> 4 1 2 3
# 1000 -> L -> 0001 -> 1
# 1000 -> R -> 0100 -> 100

# 주어진 서로 다른 A, B -> A를 B로 바꾸는 최소한의 명령어 생성

way = ('D', 'S', 'L', 'R')
sys.setrecursionlimit(10 ** 4)

def func_d(n):
    return (2 * n) % 10000


def func_s(n):
    if n == 0:
        return 9999
    return n - 1


def func_l(n):
    d1 = n // 1000
    d2 = (n // 100) % 10
    d3 = (n // 10) % 10
    d4 = n % 10
    
    return ((d2 * 10 + d3) * 10 + d4) * 10 + d1


def func_r(n):
    d1 = n // 1000
    d2 = (n // 100) % 10
    d3 = (n // 10) % 10
    d4 = n % 10

    return ((d4 * 10 + d1) * 10 + d2) * 10 + d3


t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())

    dq = deque()
    visit = [False] * 10000
    dq.append((a, ''))
    while dq:
        cur, history = dq.popleft()
        for j in range(4):
            if j == 0:
                nx = func_d(cur)
            elif j == 1:
                nx = func_s(cur)
            elif j == 2:
                nx = func_l(cur)
            else:
                nx = func_r(cur)
            
            if nx == b:
                print(history + way[j])
                break
            if not visit[nx]:
                visit[nx] = True
                nh = history + way[j]
                dq.append((nx, nh))
        if nx == b:
            break