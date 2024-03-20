# 보물섬

# 육지 L, 바다 W
# 상하좌우 육지로만 이동 가능, 한 칸에 한 시간
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 있음
# 즉, 최단 거리가 가장 긴 육지 두 곳을 찾아라
# 즉, BFS 결과의 최댓값을 찾기

# input() 하니까 시간초과남

from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, x, y):
    dq = deque()
    dq.append((i, j, 0))
    visited = [[False] * y for _ in range(x)]
    cnt = 0
    visited[i][j] = True
    while dq:
        cur_x, cur_y, cnt = dq.popleft()
        max(maximum, cnt)
        for dir in range(4):
            next_x = cur_x + dx[dir]
            next_y = cur_y + dy[dir]
            if next_x < 0 or next_x >= x or next_y < 0 or next_y >= y:
                continue
            if visited[next_x][next_y] or matrix[next_x][next_y] == 'W':
                continue
            visited[next_x][next_y] = True
            dq.append((next_x, next_y, cnt + 1))
    return cnt


x, y = map(int, input().split())

matrix = []
for _ in range(x):
    matrix.append(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False] * y for _ in range(x)]

maximum = -1

for i in range(x):
    for j in range(y):
        if matrix[i][j] == 'L':
            maximum = max(maximum, bfs(i, j, x, y))

print(maximum)