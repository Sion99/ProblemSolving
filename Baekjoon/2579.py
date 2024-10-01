# 계단 오르기

# 계단 오르는 규칙 있음
# 1. 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음
# 2. 연속된 세 개의 계단을 모두 밟으면 안됨
# 3. 마지막 도착 계단은 반드시 밟아야 함

n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))

arr = [[0, 0] for _ in range(n)]
arr[0][0] = stairs[0]

for i in range(1, n):
    arr[i][0] = max(arr[i-2][0] + stairs[i], arr[i-2][1] + stairs[i])
    arr[i][1] = arr[i-1][0] + stairs[i]

print(max(arr[n-1][0], arr[n-1][1]))