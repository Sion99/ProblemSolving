# 1로 만들기 2

# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다
# 2. X가 2로 나누어 떨어지면, 2로 나눈다
# 3. 1을 뺀다

# 정수 N이 주어졌을 때 연산을 사용하는 횟수의 최솟값

import sys

input = sys.stdin.readline

n = int(input())

# 과정을 기록해야 함!!
# arr = [[0, []] for _ in range(n)]

# arr[0][0] = 1
# arr[0][1].append(1)

# for i in range(2, n):
#     arr[i][0] = arr[i-1][0] + 1
#     arr[i][1].append(i-1)
#     if i%2 == 0:
#         arr[i][0] = arr[i//2][0]
#         arr[i][1][-1] = i//2
#     if i%3 == 0:
#         arr[i][0] = arr[i//3][0]
#         arr[i][1][-1] = i//3

# print(arr)

arr = [0] * 1000002
pre = [0] * 1000002

for i in range(2, n + 1):
    arr[i] = arr[i-1] + 1
    pre[i] = i-1
    if i%2 == 0 and arr[i] > arr[i//2] + 1:
        arr[i] = arr[i//2] + 1
        pre[i] = i//2
    if i%3 == 0 and arr[i] > arr[i//3] + 1:
        arr[i] = arr[i//3] + 1
        pre[i] = i//3

cur = n
print(arr[cur])
while True:
    print(pre[cur], end=" ")
    if cur == 1:
        break
    cur = pre[cur]