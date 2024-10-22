# 실버 2 15665. N과 M (11)

# N개의 자연수와 자연수 M
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수열을 여러 번 골라도 된다

answer = set()

def backtrack(arr, selected, n, m):
    global answer
    if len(selected) == m:
        answer.add(tuple(selected))
        return
    else:
        for i in range(n):
            selected.append(arr[i])
            backtrack(arr, selected, n, m)
            selected.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

backtrack(arr, [], n, m)

answer = sorted(answer)
for i in answer:
    print(*i)