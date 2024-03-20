# 연구소

# N x M
# 0 -> 빈 칸, 1 -> 벽, 2 -> 바이러스
# 바이러스는 상하좌우 인접한 칸으로 퍼질 수 있음
# 새로 세울 수 있는 벽은 3개, 3개 전부 세워야 함
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳 -> 안전 영역
# 안전 영역의 최댓값

# 브루트포스로 접근해보자
# 3개의 벽을 아무 빈 칸에 세운 뒤, 바이러스에 대해 BFS 진행 한 다음, 0의 개수를 세보기

from collections import deque
import copy
import sys

input = sys.stdin.readline

def bfs():
    global safezone
    temp_matrix = copy.deepcopy(matrix)
    cnt = 0
    dq = deque()
    visited = [[False] * M for _ in range(N)]
    for v in virus:
        dq.append((v[0], v[1]))
        visited[v[0]][v[1]] = True
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if temp_matrix[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] == True
                temp_matrix[nx][ny] = 2
                dq.append((nx, ny))
    for i in range(N):
        for j in range(M):
            if temp_matrix[i][j] == 0:
                cnt += 1
    safezone = max(cnt, safezone)


def make_wall(num):
    if num == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                make_wall(num + 1)
                matrix[i][j] = 0
            
    

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

virus = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            virus.append([i, j])


safezone = -1

# 벽을 3개 놓는 상황을 다 그려보자
# 첫 번째 벽, 2 번째 벽, 3번째 벽

make_wall(0)
print(safezone)

# 이번 문제는 make_wall을 재귀로 만드는 것이 관건 이었다..