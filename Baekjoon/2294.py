# 동전 2

# N 가지 동전
# 동전들의 합으로 k원 만들기 -> 동전 개수 최소!

# BFS로 접근하니까 메모리 초과 ㅜㅜ
# from collections import deque

# n, k = map(int, input().split())
# coins = set()
# for _ in range(n):
#     coins.add(int(input()))
# coins = list(coins)

# dq = deque()
# dq.append((0, 0))

# visited = [False] * 10001

# while dq:
#     money, cnt = dq.popleft()
#     for coin in coins:
#         nxmoney = money + coin
#         if nxmoney == k:
#             print(cnt + 1)
#             exit()
#         if nxmoney > k:
#             continue
#         if visited[nxmoney]:
#             continue
#         dq.append((nxmoney, cnt + 1))

# print(-1)

# DP로 접근해보기!
# 1, 5, 12
# 1 -> 1, 5, 12
# 5 -> 1, 5, 12
# 12 -> 1, 5, 12

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))

dp = [10001] * (k + 1)
dp[0] = 0

for i in range(n):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j], dp[j-coins[i]] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])

