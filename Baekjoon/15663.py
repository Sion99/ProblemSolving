# 실버 2 15663. N과 M (9)

# N개의 자연수 중에서 M개를 고른 수열

def backtrack(selected, n, m):
    global temp
    if len(selected) == m:
        temp.append(selected)
    else:
        for i in range(n):
            if not selected or selected[-1] < i:
                selected.append(i)
                backtrack(selected, n, m)
                selected.pop()


n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

temp = []
backtrack([], n, m)

temp = list(set(map(tuple, temp)))
print(temp)
for t in temp:
    for i in t:
        print(arr[i], end=' ')
    print()
