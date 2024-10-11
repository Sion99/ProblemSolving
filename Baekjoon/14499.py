# 골드 4 14499. 주사위 굴리기

# 크기 N*M인 지도가 존재한다.
# 지도 위에 주사위 하나 있으며 전개도는 다음과 같다.
#   2
# 4 1 3
#   5  
#   6

# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라본느 방향이 3인 상태로 놓여져 있으며
# 놓여져 있는 곳의 좌표는 (x, y)이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.

# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다.
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아니라면, 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

# 주사위가 이동햇을 때 마다 상단에 쓰야 있는 값을 구하는 프로그램을 작성하시오.
# 주사위는 지도의 바깥으로 이동할 수 없다. 만약 바깥으로 이동시키는 명령은 완전히 무시.

import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline

n, m, x, y, k = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))
orders = list(map(int, input().rstrip().split()))

# 가장 처음에 주사위에는 모든 면이 0으로 적혀있음
dice = [0, 0, 0, 0, 0, 0]

# 주사위는 0~5 면이 있다고 하자


dh = deque([6, 3, 1, 4])
dv = deque([6, 5, 1, 2])

# 주사위 방향 자체를 꺾지 않으니까 좀 더 단순하게 생각해도 될 듯?

ground = dh[0]
air = dh[2]

for order in orders:
    # 이동하는 명령 순서대로 진행
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

    # 주사위를 굴렸을 때, 칸 이동과 동시에 주사위가 바닥과 닿는 면도 변하겠지?
    nx = x + dx[order-1]
    ny = y + dy[order-1]
    
    # 주사위가 바깥으로 나가는 경우에는 해당 명령 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    # 이동 진행
    if order == 1:
        # 동쪽으로 굴렀을 때
        # 수평으로 증가하는 방항 (y값 증가)
        dh.rotate(1)
        ground = dh[0]
        air = dh[2]
    if order == 2:
        # 서쪽으로 굴렀을 때
        dh.rotate(-1)
        ground = dh[0]
        air = dh[2]
    if order == 3:
        # 북쪽으로 굴렸을 때
        dv.rotate(-1)
        ground = dv[0]
        air = dv[2]
    if order == 4:
        dv.rotate(1)
        ground = dv[0]
        air = dv[2]
    
    # 이동한 칸이 쓰여 있는 수 체크
    if board[nx][ny] == 0:
        # 주사위 바닥면에 있는 수가 칸에 복사됨
        board[nx][ny] = dice[ground-1]
    else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되고, 칸에 쓰여 있는 수는 0이 됨
        dice[ground-1] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny

    # 주사위 윗 면에 쓰여 있는 수 출력
    print(dice[air-1])
