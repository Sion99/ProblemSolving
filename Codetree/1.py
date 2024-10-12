# 고대 문명 유적 탐사

# 유적지는 5x5 격자
# 유물 조각은 총 7가지 1 ~ 7

# 1. 3x3 격자 선택
# 5x5 격자 내에서 3x3 격자를 선택하여 격자를 회전시킬 수 있따.
# 시계 방향으로 90, 180, 270도 회전 가능
# 선택된 격자는 항상 회전해야한다.

# 가능한 회전 방법 중 조건을 만족하는 구간을 선택한다.
# 1. 유물의 1차 획득 가치를 최대화하고
# 2. 회전을 제일 적게 한 방법 선택
# 3. 회전 중심 좌표의 열이 가장 작은 구간, 열이 같다면 행이 가장 작은 구간 선택

# 2. 유물 1차 획득
# 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결되어 있다.
# 이 조각들이 3개 이상 연결된 경우, 사라진다 (애니팡 같이 생각)
# 유물의 가치는 모인 조각의 개수와 같다.

# 6, 6, 6, 6 7, 7, 7 -> 총 7개의 조각이 사라지므로, 7의 가치 획득
# 사라진 유물 칸은 새롭게 채워진다.
# 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생겨난다.
# 새로운 조각은 열 번호가 작은 순으로 채워지고, 열 번호가 같다면 행 번호가 큰 순으로 채워진다.
# 즉, 왼쪽 끝에서부터 오른쪽으로 채워진다.

# 새로운 유물 조각이 생겨난 이후에도 조각들이 3개 이상 연결될 수 있다. 이 경우 앞과 같은 방식으로 사라지고 또 채워진다.
# 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복된다.

# 3. 탐사 반복
# 총 K번의 턴에 걸쳐 진행된다.
# 각 턴마다 획득한 유물의 가치의 총합을 출력하는 프로그램을 작성하라

import copy
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate(matrix):
    return list(map(list, zip(*matrix[::-1])))


def bfs(matrix, visited, x, y, initial):
    dq = deque()
    visited[x][y] = True
    dq.append([x, y])
    connected = [[x, y]]
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if matrix[nx][ny] != initial:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            dq.append([nx, ny])
            connected.append([nx, ny])
    if len(connected) >= 3:
        return connected
    else:
        return []


k, m = map(int, input().split())
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

backups = list(map(int, input().split()))
answer = 0

for _ in range(k):
    # 일단 어느 칸을 돌려야 최대값이 나오는지 체크
    candidates = []
    for i in range(3):
        for j in range(3):
            # 시작점 (i, j)
            matrix = []
            for k in range(3):
                matrix.append(board[i+k][j:j+3])
            matrix_90 = rotate(matrix)
            matrix_180 = rotate(matrix_90)
            matrix_270 = rotate(matrix_180)
            rotations = [matrix_90, matrix_180, matrix_270]
            for r in range(3):
                # 각각의 회전들마다 반영해서 최댓값 찾기
                temp = copy.deepcopy(board)
                for a in range(3):
                    for b in range(3):
                        temp[i+a][j+b] = rotations[k][a][b]
                # 이제 temp까지 반영을 했고, bfs 써서 연결된 영역 다 찾으면 된다!
                
                visited = [[False] * 5 for _ in range(5)]
                score = 0
                for a in range(5):
                    for b in range(5):
                        if not visited[a][b]:
                            connected = bfs(temp, visited, a, b, temp[a][b])
                            if connected:
                                score += len(connected)
                candidates.append([score, r, i, j])
    candidates.sort(key=lambda x: (-x[0], x[1], x[3], x[2]))
    
    # 만약 candidates
    # 최대값 가져오는 회전 방법 찾았고

    mx = candidates[0]
    if mx[0] == 0:
        # 만약 더 이상 찾을 유물 조각이 없다면
        break

    # 일단 1차로 획득한 유물 값 더하기
    answer += mx[0]
    print(mx)
    # 이제 유물을 모아서 없애자 (애니팡)
    matrix = []
    for k in range(3):
        matrix.append(board[mx[2]+k][mx[3]:mx[3]+3])
    for r in range(mx[1]+1):
        matrix = rotate(matrix)
    for a in range(3):
        for b in range(3):
            board[mx[2]+a][mx[3]+b] = matrix[a][b]
    visited = [[False] * 5 for _ in range(5)]
    for a in range(5):
        for b in range(5):
            if not visited:
                connected = bfs(board, visited, a, b, board[a][b])
                if connected:
                    for c in connected:
                        board[c[0]][c[1]] = 0

    for b in board:
        print(b)
                


                            