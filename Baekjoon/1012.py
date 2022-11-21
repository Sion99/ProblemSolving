# S2 유기농 배추
import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if (0 <= next_x < m) and (0 <= next_y < n):
            if matrix[next_y][next_x] == 1:
                matrix[next_y][next_x] = -1
                dfs(next_x, next_y)


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for i in range(n)]
    count = 0

    for j in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for ii in range(m):
        for jj in range(n):
            if matrix[jj][ii] == 1:
                dfs(ii, jj)
                count += 1

    print(count)
