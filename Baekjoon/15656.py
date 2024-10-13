# 실버 3 15656. N과 M (7)

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다

def backtrack(arr, selected, n, m):
    if len(selected) == m:
        for s in selected:
            print(arr[s], end=' ')
        print()
    else:
        for i in range(n):
            selected.append(i)
            backtrack(arr, selected, n, m)
            selected.pop()

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [], n, m)
