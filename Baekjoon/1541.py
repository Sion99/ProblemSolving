import sys
import re


t = (sys.stdin.readline().rstrip())
t = re.split('([+|-])', t)
# 식을 최소로 만드는 괄호
# 마이너스가 나오고 뒤에 플러스인 경우 다 괄호로 묶기
total = int(t[0])
arr = []

for i in range(1, len(t), 2):
    temp = t[i] + t[i+1]
    arr.append(int(temp))

index = 0

while (index < len(arr)):
    if arr[index] > 0:
        total += arr[index]
        index += 1
    else:
        total += arr[index]
        index += 1
        while (index < len(arr)):
            if arr[index] > 0:
                total -= arr[index]
                index += 1
            else:
                break

print(total)
