# RGB 거리

# N개의 집
# R, G, B 중 하나의 색으로 칠해야 함
# 1번 집의 색 != 2번 집의 색
# N번 집 != N-1번 집
# i번 집 != i-1 and != i+1

N = int(input())

houses = list()

for _ in range(N):
    r, g, b = map(int, input().split())
    houses.append([r, g, b])

# 처음에 세가지 색이 있으니, 제일 작은 것을 선택해본다.
# 다음 선택은, 첫 번째 선택한 것을 제외한 색 중 가장 작은 것
# 다음 선택은, 나머지 하나 자동선택
# 결국 R, G, B, R, G, B 거나
# G, R, B, G, R, B 거나
# G, B, R, G, B, R 거나
# R, B, G, R, B, G 거나
# B, R, G, B, R, G 거나
# B, G, R, B, G, R 중 하나의 형태
# 이 중에서 최솟값을 찾아야 하는 문제
    
dp = [[0]*3 for _ in range(N)]

dp[0][0], dp[0][1], dp[0][2] = houses[0][0], houses[0][1], houses[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] + houses[i][0], dp[i - 1][2] + houses[i][0])
    dp[i][1] = min(dp[i - 1][0] + houses[i][1], dp[i - 1][2] + houses[i][1])
    dp[i][2] = min(dp[i - 1][0] + houses[i][2], dp[i - 1][1] + houses[i][2])

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))