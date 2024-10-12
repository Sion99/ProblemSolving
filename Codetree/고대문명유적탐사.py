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
    dq = deque([(x, y)])
    visited[x][y] = True
    connected = [(x, y)]
    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 5 and 0 <= ny < 5 and matrix[nx][ny] == initial and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
                connected.append((nx, ny))
    return connected if len(connected) >= 3 else []


def calculate_score(matrix):
    visited = [[False] * 5 for _ in range(5)]
    score = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j] and matrix[i][j] != 0:
                connected = bfs(matrix, visited, i, j, matrix[i][j])
                if connected:
                    score += len(connected)
                    for x, y in connected:
                        matrix[x][y] = 0
    return score


def fill_empty_spaces(matrix, backups):
    for j in range(5):
        empty_count = 0
        for i in range(4, -1, -1):
            if matrix[i][j] == 0:
                empty_count += 1
            elif empty_count > 0:
                matrix[i+empty_count][j] = matrix[i][j]
                matrix[i][j] = 0

        for i in range(empty_count):
            matrix[i][j] = backups.pop(0)
            if not backups:
                backups.extend(list(range(1, 8)))


def find_best_rotation(board):
    candidates = []
    for i in range(3):
        for j in range(3):
            matrix = [row[j:j+3] for row in board[i:i+3]]
            for r in range(3):
                rotated = rotate(matrix) if r > 0 else matrix
                temp = copy.deepcopy(board)
                for a in range(3):
                    for b in range(3):
                        temp[i+a][j+b] = rotated[a][b]
                score = calculate_score(copy.deepcopy(temp))
                candidates.append((score, r+1, i, j))
    return max(candidates, key=lambda x: (-x[0], x[1], x[3], x[2]))


k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
backups = list(map(int, input().split()))
total_score = 0

for _ in range(k):
    best_score, rotations, i, j = find_best_rotation(board)
    if best_score == 0:
        break

    total_score += best_score

    matrix = [row[j:j+3] for row in board[i:i+3]]
    for _ in range(rotations):
        matrix = rotate(matrix)
    for a in range(3):
        for b in range(3):
            board[i+a][j+b] = matrix[a][b]

    while True:
        score = calculate_score(board)
        if score == 0:
            break
        total_score += score
        fill_empty_spaces(board, backups)

print(total_score)
