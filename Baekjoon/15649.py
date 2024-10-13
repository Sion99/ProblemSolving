# 실버 3 15649. N과 M (1)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하라
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# nCm

def backtrack(selected, start, n, m):
    global arr
    if len(selected) == m:
        for s in selected:
            print(arr[s], end=' ')
        print()
    else:
        for i in range(n):
            if i not in selected:
                selected.append(i)
                backtrack(selected, start+1, n, m)
                selected.pop()


n, m = map(int, input().split())

arr = [1, 2, 3, 4, 5, 6, 7, 8]

backtrack([], 0, n, m)