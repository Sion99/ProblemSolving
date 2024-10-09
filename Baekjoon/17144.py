# 골드 4 17144. 미세먼지 안녕!

# 집은 R*C 격자판
# 공기청정기는 항상 1번 열에 설치되어 있고 2 행을 차지한다.
# 공기청정기가 설치되지 않은 칸에는 미세먼지가 있다.

# 1초 동안 다음이 순서대로 일어난다.

# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
#   - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
#   - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
#   - 확산되는 양은 A(r, c) // 5 이다.
#   - (r, c)에 남은 미세먼지 양은 A(r, c) - (확산된 방향 수) * (A(r, c) // 5)

# 2. 공기청정기가 작동한다.
#   - 공기청정기에서는 바람이 나온다.
#   - 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환
#   - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다
#   - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

# 일단 확산까지는 쉽고, 공기청정기 바람을 좀 생각을 해봐야 할 듯?
# 확산까지 만들어보고, 그 다음 천천히 해보자.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

import sys

input = sys.stdin.readline

r, c, t = map(int, input().rstrip().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().rstrip().split())))

ap = 0
for i in range(r):
    if board[i][0] == -1:
        # 공기청정기 위치 찾기
        ap = i
        break

for _ in range(t):
    # 1초 지날때마다 수행
    # 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 진행
    dust = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 미세먼지 칸인 경우 인접한 네 방향으로 확산
            if board[i][j] > 0:
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if board[nx][ny] == -1:
                        continue
                    dust[nx][ny] += (board[i][j] // 5)
                    dust[i][j] -= (board[i][j] // 5)
    
    # 미세먼지 확산 완료!
    for i in range(r):
        for j in range(c):
            board[i][j] += dust[i][j]
    
    # 2. 공기청정기가 작동한다.
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    # 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    # 공기청정기는 [ap][0], [ap+1][0]에 위치해있다. 따라서
    # 바람이 불어서 들어오는 경로는
    # 위쪽: (ap, 0) -> (ap, c-1) -> (0, c-1) -> (0, 0) -> (ap, 0) 방향으로 들어간다.
    # 아래쪽: (ap+1, 0) -> (ap+1, c-1) -> (r-1, c-1) -> (r-1, 0) -> (ap+1, 0) 방향으로 들어간다.

    # 바람이 불어오는 역으로 생각을 해야겠는데? 
    for i in range(ap-1, 0, -1):
        board[i][0] = board[i-1][0]
        # 그냥 한 칸 씩 땡겨오기
    for i in range(c-1):
        board[0][i] = board[0][i+1]
    for i in range(ap):
        board[i][c-1] = board[i+1][c-1]
    for i in range(c-1, 0, -1):
        board[ap][i] = board[ap][i-1]
    board[ap][1] = 0

    # 아래도 처리
    for i in range(ap+2, r-1):
        board[i][0] = board[i+1][0]
    for i in range(c-1):
        board[r-1][i] = board[r-1][i+1]
    for i in range(r-1, ap, -1):
        board[i][c-1] = board[i-1][c-1]
    for i in range(c-1, 0, -1):
        board[ap+1][i] = board[ap+1][i-1]
    board[ap+1][1] = 0

ans = 0
for b in board:
    ans += sum(b)

ans += 2
print(ans)