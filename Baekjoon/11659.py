# 구간 합 구하기 4

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하라
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i-1] + arr[i - 1]

for i in range(m):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])