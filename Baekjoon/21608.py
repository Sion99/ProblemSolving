# 골드 5 21608. 상어 초등학교

# 교실 N*N 격자
# 학생수 N^2명
# 학생은 1번부터 N*2 번까지 번호가 매겨짐

# 학생의 순서 및 각 학생이 좋아하는 학생 4명 모두 조사 완료
# 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다.
# 상하좌우 거리가 1인 칸이 인접하다고 함

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 일단, 좋아하는 학생들이 가장 많이 서로 앉을 수 있께 배치
# 단, 학생 입력받은 순서대로 처리해야 함

# 학생의 만족도를 구해야 한다.
# 학생의 만족도는 자리 배치가 모두 끝난 후에 할 수 있다.
# 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
# 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 100, 4 -> 1000
# 한 번에 풀어버리기~

import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline

n = int(input().rstrip())
board = [[0]*n for _ in range(n)]

priority = []
for _ in range(n**2):
    arr = list(map(int, input().rstrip().split()))
    priority.append(arr)
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 곳으로 자리를 정한다.
    candidate = []
    for i in range(n):
        for j in range(n):
            # 일단 비어있는 곳 찾아서 상하좌우 인접한 곳에 좋아하는 학생 있는지 체크
            if board[i][j] == 0:
                # 비어있다면?
                friend_cnt = 0
                empty_cnt = 0
                for dir in range(4):
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] in arr:
                        # 좋아하는 학생 자리라면
                        friend_cnt += 1
                    if board[nx][ny] == 0:
                        # 비어있다면
                        empty_cnt += 1
                    candidate.append([i, j, friend_cnt, empty_cnt])
    candidate.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    x, y = candidate[0][0], candidate[0][1]
    board[x][y] = arr[0]

# 자리 배치 다 끝났으니 만족도 조사합시다
# 모든 학생 돌면서, 그 학생이 좋아하는 학생들과 인접하게 배치되었는지 체크
# 0 -> 0, 1 -> 1, 2 -> 10, 3 -> 100, 4 -> 1000

priority.sort(key=lambda x:x[0])

answer = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        cur = board[i][j]
        ## 학생 번호 cur 차례
        ## cur 학생이 좋아하는 친구들 목록
        ## priority[cur-1][1:4]
        for dir in range(4):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] in priority[cur-1]:
                cnt += 1
        if cnt > 0:
            answer += 10**(cnt-1)

print(answer)