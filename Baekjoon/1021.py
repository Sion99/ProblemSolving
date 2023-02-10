from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i + 1)

arr = deque(arr)

count = 0
list = list(map(int, input().split()))
for i in list:
    if arr.index(i) > len(arr) / 2:
        while True:
            if arr.index(i) == 0:
                break
            arr.rotate(1)
            count += 1
    else:
        while True:
            if arr.index(i) == 0:
                break
            arr.rotate(-1)
            count += 1
    arr.popleft()

print(count)
