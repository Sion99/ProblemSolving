# 실버 3 계단오르기

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


# 계단 오르기 규칙
# 1. 계단은 한 번에 한 계단 또는 두 계단씩 오를 수 있다
# 2. 연속된 세 개의 계단을 모두 밟아서는 안된다 (한 계단씩 세번은 안됨)
# 3. 마지막 도착 계단은 반드시 밟아야 함

i = 0
check = 0
dp = []
while (i < len(arr)):
    if arr[i+1] > arr[i+2]:
        if check == 2:
            i += 2
            check = 1
            dp.append(dp[-1]+arr[i])
        else:
            i += 1
            check += 1
            dp.append(dp[-1]+arr[i])
    else:
        i += 2
        check = 1
        dp.append(dp[-1]+arr[i])

print(dp)
