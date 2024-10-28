# 실버 2 6603. 로또

# 1~49 중 수 6개 고르기
# 49가지 수 중 6개 초과 집합 S를 만들어 그 원소만 가지고 번호를 선택하는 방법
# 집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하라

def backtrack(arr, selected, idx, k):
    if len(selected) == 6:
        for s in selected:
            print(arr[s], end= ' ')
        print()
    else:
        for i in range(idx, k):
            selected.append(i)
            backtrack(arr, selected, i+1, k)
            selected.pop()

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    k = arr[0]
    arr = arr[1:]
    backtrack(arr, [], 0, k)
    print()
