# RGB 주차장

# N칸으로 이루어진 주차장을 R, G, B로 색칠
# 주차장의 각 칸은 인접한 칸과 색이 다름

# 주차장의 첫째 칸은 어떤 색상이든 상관없음 -> 주차장을 색칠할 수 있는 경우의 수
# 비용은 아니고, 그냥 경우의 수네

# R, G, B, G, R, G, B, G, R ...
# R, G, B, R, G, B, R, G, B ...
# G, B, R, B, R, G, B, R, G ...

import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = [[0, 0, 0] for _ in range(n)]

# R, G, B 스타트 각각으로 마지막 n번째 칸에서 경우 다 합치면 되겠다

arr[0][0] = 1
arr[0][1] = 1
arr[0][2] = 1

for i in range(1, n):
	arr[i][0] = (arr[i-1][1] + arr[i-1][2]) % 100000007
	arr[i][1] = (arr[i-1][0] + arr[i-1][2]) % 100000007
	arr[i][2] = (arr[i-1][0] + arr[i-1][1]) % 100000007
	
print((arr[n-1][0] + arr[n-1][1] + arr[n-1][2])%100000007)

# print(3*2**(n-1)%100000007)
