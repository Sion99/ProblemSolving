# 파이프 옮기기

# N x N 격자판
# 파이프 하나당 2개의 연속된 칸 차지
# 파이프 수평, 수직, 대각선 가능
# 단, 한 번에 최대 45도 (대각선) 만 꺾을 수 있음


# 시간 초과 난 BFS 코드

# from collections import deque

# def horiziontal(r, c):
#     if c + 1 < N:
#         if matrix[r][c + 1] == 0:
#             dq.append((r, c + 1, 0))
#     if r + 1 < N and c + 1 < N:
#         if matrix[r + 1][c + 1] == 0 and matrix[r][c + 1] == 0 and matrix[r + 1][c] == 0:
#             dq.append((r + 1, c + 1, 2))

# def vertical(r, c):
#     if r + 1 < N:
#         if matrix[r + 1][c] == 0:
#             dq.append((r + 1, c, 1))
#     if r + 1 < N and c + 1 < N:
#         if matrix[r + 1][c + 1] == 0 and matrix[r][c + 1] == 0 and matrix[r + 1][c] == 0:
#             dq.append((r + 1, c + 1, 2))

# def diagonal(r, c):
#     if c + 1 < N:
#         if matrix[r][c + 1] == 0:
#             dq.append((r, c + 1, 0))
#     if r + 1 < N:
#         if matrix[r + 1][c] == 0:
#             dq.append((r + 1, c, 1))
#     if r + 1 < N and c + 1 < N:
#         if matrix[r + 1][c + 1] == 0 and matrix[r][c + 1] == 0 and matrix[r + 1][c] == 0:
#             dq.append((r + 1, c + 1, 2))

# N = int(input())

# matrix = []
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))

# if matrix[N - 1][N - 1]:
#     print(0)
#     exit()

# dq = deque()
# dq.append((0, 1, 0))
# cnt = 0
# while dq:
#     r, c, dir = dq.popleft()
#     if r == N - 1 and c == N - 1:
#         cnt += 1
#         continue
#     if dir == 0:
#         horiziontal(r, c)
#     elif dir == 1:
#         vertical(r, c)
#     else:
#         diagonal(r, c)

# print(cnt)

def dfs(r, c, dir):
    global cnt
    if r == N - 1 and c == N - 1:
        cnt += 1
        return
    if dir == 0 or dir == 2:
        if c < N - 1:
            if matrix[r][c + 1] == 0:
                dfs(r, c + 1, 0)
    if dir == 1 or dir == 2:
        if r < N - 1:
            if matrix[r + 1][c] == 0:
                dfs(r + 1, c, 1)
    if dir == 0 or dir == 1 or dir == 2:
        if r < N - 1 and c < N - 1:
            if matrix[r + 1][c] == 0 and matrix[r][c + 1] == 0 and matrix[r + 1][c + 1] == 0:
                dfs(r + 1, c + 1, 2)


N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

cnt = 0

if matrix[N - 1][N - 1]:
    print(cnt)
    exit()

dfs(0, 1, 0)
print(cnt)
