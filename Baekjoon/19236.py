# 골드 2 19236. 청소년 상어

# 4x4 크기의 공간이 있다
# 한 칸에는 물고기가 한 마리 존재하고 각 물고기는 번호와 방향을 가지고 있다.
# 번호는 1~16 사이 자연수
# 중복되는 번호는 없다.
# 방향은 8가지 방향

# 청소년 상어는 (0, 0)에 있는 물고기를 먹고 (0, 0)에 들어가게 된다.
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

# 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
# 물고기는 한 칸을 이동할 수 있다.
# 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
# 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸
# 각 물고기는 방향이 이동할 수 있는 칸을 향할 때 까지 반시계 방향으로 45도 회전한다.
# 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
# 그 외의 경우에는 그 칸으로 이동을 한다.
# 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

# 물고기의 이동이 모두 끝나면 상어가 이동한다.
# 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
# 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
# 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
# 물고기가 없는 칸으로는 이동할 수 없다.
# 상어가 이동할 수 있는 칸이 없으면 집으로 간다. (게임 종료)
# 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 과정에 반복된다.

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값

import sys
import copy

# 8가지 방향, 반시계방향으로 돈다.
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 이동 함수
def move_fish(board, alive, sx, sy):
    for a in alive:
        moved = False
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == a:  # 물고기 번호가 맞는 물고기를 찾는다.
                    for dir in range(board[i][j][1], board[i][j][1] + 8):
                        nx = i + dx[dir % 8]
                        ny = j + dy[dir % 8]
                        # 경계 밖이거나 상어가 있으면 이동하지 않는다.
                        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                            continue
                        if nx == sx and ny == sy:
                            continue
                        # 위치 변경
                        board[i][j][1] = dir % 8  # 방향을 갱신
                        board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                        moved = True
                        break
                if moved:
                    break
            if moved:
                break


# 백트래킹 함수
def backtrack(board, alive, shark, total):
    global answer

    board = copy.deepcopy(board)
    alive = copy.deepcopy(alive)

    # 상어가 현재 위치의 물고기를 먹는다.
    total += board[shark[0]][shark[1]][0]
    sd = board[shark[0]][shark[1]][1]  # 상어가 물고기의 방향을 가져간다.
    alive.remove(board[shark[0]][shark[1]][0])  # 물고기가 죽음
    board[shark[0]][shark[1]][0] = 0
    
    # 물고기 이동
    move_fish(board, alive, shark[0], shark[1])

    # 상어가 이동할 수 있는 칸으로 이동
    moved = False
    for step in range(1, 4):
        nx = shark[0] + dx[sd] * step
        ny = shark[1] + dy[sd] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny][0] > 0:  # 물고기가 있는 칸만 갈 수 있음
            moved = True
            backtrack(board, alive, [nx, ny], total)

    # 더 이상 이동할 곳이 없으면 최댓값 갱신
    if not moved:
        answer = max(answer, total)


input = sys.stdin.readline

board = [[] for _ in range(4)]
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(4):
        board[i].append([arr[2 * j], arr[2 * j + 1] - 1])  # 방향은 0~7로 맞추기 위해 -1

answer = 0
alive = [i for i in range(1, 17)]  # 살아있는 물고기 번호 리스트

# 백트래킹 시작
backtrack(board, alive, [0, 0], 0)

print(answer)
