# 실버 3 15652. N과 M (4)

# 1부터 N 중에 M개 고른 ㅅ열
# 같은 수를 여러 번 골라도 된다
# 고른 수열은 비내림차순

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

arr = [1, 2, 3, 4, 5, 6, 7, 8]

backtrack(arr, [], n, m)