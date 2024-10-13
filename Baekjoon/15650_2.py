# 실버 3 15650. N과 M (2)

# 자연수 N과 M 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

def backtrack(arr, selected, start, n, m):
    if len(selected) == m:
        # 고른 수열이 오름차순인지 체크
        for s in selected:
            print(arr[s], end=' ')
        print()
    else:
        for i in range(start, n):
            selected.append(i)
            backtrack(arr, selected, i+1, n, m)
            selected.pop()



n, m = map(int, input().split())

arr = [1, 2, 3, 4, 5, 6, 7, 8]

backtrack(arr, [], 0, n, m)