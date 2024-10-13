# 실버 3 15651. N과 M (3)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하라

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

arr = [1, 2, 3, 4, 5, 6, 7]

backtrack(arr, [], n, m)