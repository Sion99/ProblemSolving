# 1767. [SW Test 샘플문제] 프로세서 연결하기

# 프로세서는 N*N 셀로 되어있다.
# 1개의 셀에는 1개의 코어 또는 전선이 올 수 있다.
# 프로세서의 가장자리에는 전원이 흐르고 있고, 코어와 전원을 연결하는 전선은 직선만 가능
# 전선은 절대로 교차되어서 안된다.

# 초기 상태 프로세서 정보가 주어질 때, 최대한 많은 코어에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
# 단 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = []
    # 초기 프로세서 상태
    for i in range(n):
        board.append(list(map(int, input().split())))
    cnt = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # 코어 발견 시
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    # 벽에 붙어 있다면 길이 0으로 취급
                    continue
                # 그게 아니라면, 4가지 방면 벽과의 거리를 재고, 최솟값을 고른다 (가급적)
                # 현 위치가 (i, j) 일 때 갈 수 있는 네 방향의 벽
                # (i, 0) (0, j) (i, n) (n, j)
                mn = n
                # 왼쪽으로 갈 수 있는지 체크
                left, right, up, down = 0, 0, 0, 0
                for y in range(j, -1, -1):
                    if board[i][y] != 0:
                        left = 9999
                        break
                    left += 1
                # 오른쪽으로 갈 수 있는지 체크
                for y in range(j, n):
                    if board[i][y] != 0:
                        right = 9999
                        break
                    right += 1
                # 위로 갈 수 있는지 체크
                for x in range(i, -1, -1):
                    if board[x][j] != 0:
                        up = 9999
                        break
                    up += 1
                # 아래로 갈 수 있는지 체크
                for x in range(i, n):
                    if board[x][j] != 0:
                        down = 9999
                        break
                    down += 1
                
                