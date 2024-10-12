# 골드 5 15686. 치킨 배달

# 크기가 N*N 도시

# 각 칸은 비어있거나, 치킨집, 일반 집 중 하나

# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가짐
# 도시의 치킨 거리 = 모든 치킨 거리 총합
# 맨해튼 거리로 계산

# 0 빈칸 1 집 2 치킨집

# 일부 치킨집을 폐업하고, 도시에서 가장 많은 수익을 낼 수 있는 치킨집 최대 M개 고르기
# 도시의 치킨 거리를 최소화 하면서 최대 M개만 골라라

import copy
import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input = sys.stdin.readline

def city_cd(board, chicken_list, selected_list, n):
    total = 0
    selected_chicken = []
    for s in selected_list:
        selected_chicken.append(chicken_list[s])
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                total += chicken_distance(selected_chicken, i, j)
    return total

def chicken_distance(chicken_list, i, j):
    ans = 10000
    for c in chicken_list:
        ans = min(ans, abs(i-c[0]) + abs(j-c[1]))
    return ans

# def chicken_distance(board, i, j, n):
#     visited = [[-1] * n for _ in range(n)]
#     dq = deque()
#     dq.append((i, j))
#     visited[i][j] = 0
#     while dq:
#         x, y = dq.popleft()
#         if board[x][y] == 2:
#             return visited[x][y]
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if visited[nx][ny] != -1:
#                 continue
#             visited[nx][ny] = visited[x][y] + 1
#             dq.append((nx, ny))

def backtrack(original_board, chicken_list, selected_list, start, m):
    global ans, n
    # 일단 치킨집에서 m개 고르는 것
    # 최대 m개를 고르고 치킨 거리를 가장 작은 값을 구하라고 하는데,
    # 무조건 m개 고르는 것이 치킨 거리 최솟값을 보장한다.
    # 반대로 생각해서, 폐업시킬 치킨집을 (치킨집수-m)개 고르고
    # 해당 치킨집 폐업 때리고 남아있는 치킨집 (m개) 에 대한 치킨 거리 계산하는게 낫네

    # 일단 m개 고를 수 있게 해줘
    if len(selected_list) == m:
        # 다 골랐으면 멈추고 도시 치킨 거리 최솟값 구해야지
        ans = min(ans, city_cd(board, chicken_list, selected_list, n))
        return
    else:
        # 만약 아직 고르고 있다면
        for i in range(start, len(chicken_list)):
            selected_list.append(i)
            backtrack(original_board, chicken_list, selected_list, i+1, m)
            selected_list.pop()
            


n, m = map(int, input().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

ans = 10000

chicken_list = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken_list.append([i, j])

# total_chicken = len(chicken_list)
# # 폐업시킬 치킨집 수
# closing = total_chicken - m

# 이제 치킨집이 M개 남을 때 까지 하나씩 줄여 가면서 치킨 거리를 계산해본다.
backtrack(board, chicken_list, [], 0, m)
print(ans)