# 실버 2 15664. N과 M (10)

# N개의 자연수, 자연수 M
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순

answer = []

def backtrack(arr, selected, n, m, start):
    global answer
    if len(selected) == m:
        temp = [arr[s] for s in selected]
        if temp not in answer:
            answer.append(temp)
        return
    else:
        for i in range(start, n):
            if i not in selected:
                selected.append(i)
                backtrack(arr, selected, n, m, i)
                selected.pop()


n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()


backtrack(arr, [], n, m, 0)

for a in answer:
    for s in a:
        print(s, end=' ')
    print()