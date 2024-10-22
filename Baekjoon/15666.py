# 실버 2 15666. N과 M (12)

# N개의 자연수, 자연수 M
# N개의 자연수에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다
# 고른 수열은 비내림차순

answer = set()

def backtrack(arr, selected, n, m, start):
    if len(selected) == m:
        answer.add(tuple(selected))
    else:
        for i in range(start, n):
            selected.append(arr[i])
            backtrack(arr, selected, n, m, i)
            selected.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [], n, m, 0)

answer = sorted(answer)
for i in answer:
    print( *i)