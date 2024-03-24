# 아기 상어 (2트)

# 기존 풀이가 너무 오래 걸리고, 탐색 우선순위 조건을 만족하지 못하여 다시 작성

# 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다
# 상어는 자신의 크기와 같은 물고기는 먹지 못하고 지나만 갈 수 있다
# 상어는 자신의 크기보다 큰 물고기는 벽으로 인식한다

# 상어의 가장 마지막 위치를 기록하는 변수를 두자

import sys
from collections import deque

input = sys.stdin.readline

# 북, 서, 동, 남
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

last_x, last_y, time = 0, 0, 0

def bfs(size):
    global last_x, last_y, time
    fish_to_eat = []
    visited = [[False] * N for _ in range(N)]
    dq = deque()
    dq.append((last_x, last_y, 0))
    matrix[last_x][last_y] = 0
    visited[last_x][last_y] = True
    while dq:
        x, y, cnt = dq.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or matrix[nx][ny] > size:
                continue
            # 만약 사이즈가 작다 -> 먹이 발견! -> 이게 과연 가장 가까우면서 조건에 맞는 고기인가?
            if 0 < matrix[nx][ny] < size:
                fish_to_eat.append((cnt + 1, nx, ny))
            visited[nx][ny] = True
            dq.append((nx, ny, cnt + 1))

    if not fish_to_eat:
        return False
    
    fish_to_eat.sort()
    dist, last_x, last_y = fish_to_eat[0]
    matrix[last_x][last_y] = 0
    time += dist
    return True
    

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            last_x = i
            last_y = j
            break

size = 2
eaten = 0
while True:
    if bfs(size):
        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0
    else:
        break

print(time)