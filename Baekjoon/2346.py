from collections import deque

n = int(input())
temp = list(map(int, input().split()))

arr = []
idx = 1
for i in range(len(temp)):
    arr.append([temp[i], idx])
    idx += 1

arr = deque(arr)

answer = []
while (True):
    (last, index) = arr.popleft()
    answer.append(index)
    if last > 0:
        arr.rotate(1 - last)
    else:
        arr.rotate(-last)
    if (len(arr) == 0):
        break

print(*answer)
