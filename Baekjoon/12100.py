# 골드 1 12100. 2048(Easy)

# 2048 게임은 NxN 보드에서 진행됨
# 한 번의 이동 -> 전체 블록을 상하좌우 네 방향 중 하나로 이동하는 것
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 됨
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.

# 여기서 이동을 한 번 할 때마다 블록이 추가되지 않는다. 즉 블록은 초기 상태에서 시작

# 합쳐지는 로직만 신경 잘 쓰면 될 듯?
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하라

import copy

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 상하좌우로 전체 블록을 밀어버릴 수 있음!!
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록 -> 그냥 전부 5번 이동시켜서 비교

def push_up(board):
    # 제일 위부터 합쳐진다
    for j in range(len(board)):
        cur = 0
        for i in range(len(board)):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[cur][j] == 0:
                    board[cur][j] = temp                
                elif board[cur][j] == temp:
                    board[cur][j] *= 2
                    cur += 1
                else:
                    cur += 1
                    board[cur][j] = temp
    return board

def push_down(board):
    # 제일 아래부터 합쳐진다
    for j in range(len(board)):
        cur = len(board) - 1
        for i in range(len(board)-1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[cur][j] == 0:
                    board[cur][j] = temp
                elif board[cur][j] == temp:
                    board[cur][j] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[cur][j] = temp
    return board

def push_left(board):
    for i in range(len(board)):
        cur = 0
        for j in range(len(board)):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][cur] == 0:
                    board[i][cur] = temp
                elif board[i][cur] == temp:
                    board[i][cur] *= 2
                    cur += 1
                else:
                    cur += 1
                    board[i][cur] = temp
    return board

def push_right(board):
    for i in range(len(board)):
        cur = len(board)-1
        for j in range(len(board)-1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][cur] == 0:
                    board[i][cur] = temp
                elif board[i][cur] == temp:
                    board[i][cur] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[i][cur] = temp
    return board


def backtrack(board, move):
    global answer
    if move == 5:
        # 전부 이동 완료
        mx = 0
        for i in range(len(board)):
            for j in range(len(board)):
                mx = max(mx, board[i][j])
        answer = max(answer, mx)
    else:
        for dir in range(4):
            temp = copy.deepcopy(board)
            if dir == 0:
                # 위로 밀기
                temp = push_up(temp)
            if dir == 1:
                # 아래로 밀기
                temp = push_down(temp)
            if dir == 2:
                # 왼쪽으로 밀기
                temp = push_left(temp)
            if dir == 3:
                # 오른쪽으로 밀기
                temp = push_right(temp)
            # 밀었으면 현 상태를 다음으로 넘기기
            backtrack(temp, move+1)


answer = 0

backtrack(board, 0)

print(answer)