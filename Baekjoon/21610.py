# 골드 5 21610. 마법사 상어와 비바라기

# 비바라기를 시전하면 하늘에 비구름을 만들 수 있다.
# N * N 격자에서 연습
# 격자의 각 칸에는 바구니가 하나 있고, 바구니는 물을 제한 없이 저장할 수 있다

# (1, 1) 부터 (N, N) 까지 존재
# 무한히 확장될 수 있기 때문에 범위를 넘어가면 다시 돌아옴

# 비바라기 시전하면 (N, 1) (N, 2) (N-1, 1), (N-1, 2)에 비구름 생김
# 구름에 이동 M번 명령
# 이동 명령은 방향 d와 거리 s로 이루어짐
# 방향은 총 8개 방향
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙

# 이동을 명령하면 다음이 순서대로 진행된다.
# 1. 모든 구름이 d 방향으로 s칸 이동한다
# 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 3. 구름이 모두 사라진다.
# 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법 시전
#   - 물복사버그란 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c) 칸 물이 증가한다.
#   - 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다. 즉 경계를 명확히 지으면 됨
# 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구하라

import sys

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

cloud = [[False] * n for _ in range(n)]

# 처음에 비바라기 시전했으니까 초기 세팅해주기
# (N-1, 0) (N-1, 1) (N-2, 0), (N-2, 1)
cloud[n-1][0], cloud[n-1][1], cloud[n-2][0], cloud[n-2][1] = True, True, True, True


for _ in range(m):
    d, s = map(int, input().rstrip().split())
    # 1. 모든 구름이 d 방향으로 s 칸 이동한다.
    move = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == True:
                # 새롭게 이동한 자리가 초과할 수 있잖아?
                # 그럴 때는 N으로 나눠주면 되지 않을까?
                nx = (i + s*dx[d-1]) % n
                ny = (j + s*dy[d-1]) % n
                move[nx][ny] = True
    # 구름 이동 완료
    cloud = move

    
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == True:
                board[i][j] += 1
    
    # 3. 구름이 모두 사라진다.

    # 4. 2에서 물이 증가한 칸(구름이 있었던 칸)에 물복사버그 마법을 시전한다.
    # 대각선 방향만 이었음..!
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == True:
                for dir in range(4):
                    nx = i + dx[2*dir + 1]
                    ny = j + dy[2*dir + 1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] > 0:
                        # 물이 존재하는 칸 개수 만큼 물복사
                        board[i][j] += 1
    
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    ncloud = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not cloud[i][j]:
                board[i][j] -= 2
                ncloud[i][j] = True
    
    cloud = ncloud


# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.

ans = 0
for b in board:
    ans += sum(b)       
print(ans)
    
