# N과 M (8)
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하기

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다
# 고른 수열은 비내림차순

# 비내림차순의 중복조합 구하기

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

prod = list(set(combinations_with_replacement(num, M)))
prod.sort()

for p in prod:
    ans = list(p)
    ans.sort()
    for i in ans:
        print(i, end=" ")
    print()