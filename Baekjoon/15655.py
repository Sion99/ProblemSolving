# 실버 3 15655. N과 M (6)

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다

def backtrack(arr, selected, n, m):
    if len(selected) == m:
        for s in selected:
            print(arr[s], end=' ')
        print()
    else:
        for i in range(n):
            if not selected or selected[-1] < i:
                selected.append(i)
                backtrack(arr, selected, n, m)
                selected.pop()

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [], n, m)
