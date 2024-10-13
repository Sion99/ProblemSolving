# 실버 3 15657. N과 M (8)

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수 여러 번 가능
# 비내림차순

def backtrack(arr, selected, n, m):
    if len(selected) == m:
        for s in selected:
            print(arr[s], end=' ')
        print()
    else:
        for i in range(n):
            if not selected or selected[-1] <= i:
                selected.append(i)
                backtrack(arr, selected, n, m)
                selected.pop()

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [], n, m)