# 골드 3 1941. 소문난 칠공주

# 총 25명의 여학생들로 이루어진 여학생반은 5x5의 정사각형 격자 형태
# 이다솜파 vs 임도연파

# 소문난 칠공주는 다음과 같은 규칙을 만족한다.
# 1. 7명의 여학생들로 구성
# 2. 7명의 자리는 서로 가로나 세로로 인접해야함
# 3. 반드시 이다솜파 학생들로만 구성될 필요는 없음
# 4. 이다솜파가 반드시 우위를 점할 것, 7명 중 4명 이상은 이다솜파여야 함

# 여학생반의 자리 배치도가 주어졌을 때 소문난 칠공주를 결성할 수 있는 모든 경우의 수

# 자리는 최초에 한 번 정해진 것으로 끝

# 일단, 무작위로 7명 고르고 -> 이다솜파가 4명 이상인지 체크 -> 모든 자리가 이어졌는지 체크 -> 통과하면 cnt += 1

# 25명 중 7명 고르는 것
# 0 ~ 24 -> (0, 0) (0, 1) (0, 2) ... (4, 4) 느낌으로 고르면 될 듯?

from collections import deque

def count_s(selected):
    global board
    cnt_s = 0
    for s in selected:
        if board[s//5][s%5] == 'S':
            cnt_s += 1
    if cnt_s >= 4:
        return True
    return False


def bfs(selected):
    board = [[0 for _ in range(5)] for _ in range(5)]
    visited = [[False for _ in range(5)] for _ in range(5)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for s in selected:
        board[s//5][s%5] = 1
    
    x = selected[0] // 5
    y = selected[0] % 5
    visited[x][y] = True
    dq = deque()
    dq.append((x, y))
    cnt = 0
    while dq:
        x, y = dq.popleft()
        cnt += 1
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if board[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            dq.append((nx, ny))
    
    if cnt == 7:
        return True
    return False


def backtrack(selected, idx):
    global answer
    if len(selected) == 7:
        if count_s(selected):
            if bfs(selected):
                answer += 1
        return
    else:
        for i in range(idx, 25):
            selected.append(i)
            backtrack(selected, i+1)
            selected.pop()

board = []
for _ in range(5):
    board.append(list(input()))

answer = 0

backtrack([], 0)

print(answer)