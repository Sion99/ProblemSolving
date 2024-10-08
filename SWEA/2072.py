# 2072 홀수만 더하기

# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램 작성하라

t = int(input())

for j in range(t):
    arr = list(map(int, input().split()))
    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            continue
        else:
            total += arr[i]
    print(f"#{j+1} {total}")