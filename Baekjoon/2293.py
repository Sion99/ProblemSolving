# 동전 1

# n가지 종류 동전 사용해서 합이 k되는 경우의 수

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

print(coins)

# 일단 최소 단위를 가장 많이 사용해서 k를 만드는 경우를 생각..?
# 아니면 최대 단위를 이용해서 가장 적게 사용해 k를 만드는 경우를 생각할까..?




for i in range(n):
    if 