# N과 M (5)

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하기
# N개의 자연수 중에서 M개를 고른 수열
# nPm

import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

perm = list(permutations(num, M))

for p in perm:
    for i in range(len(p)):
        print(p[i], end=" ")
    print()