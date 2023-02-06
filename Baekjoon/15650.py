from itertools import combinations

n, m = map(int, input().split())

arr = list()
for i in range(1, n + 1):
    arr.append(i)

per = list(combinations(arr, m))
per.sort()
for i in per:
    print(*i)
