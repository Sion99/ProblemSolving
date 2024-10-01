# 1로 만들기

# 1. X가 3으로 나누어 떨ㅇ어지면 3으로 나눈다
# 2. X가 2로 나누어 떨어지면 2로 나눈다
# 3. 1을 뺀다

# 연산을 사용하는 횟수 최솟값

n = int(input())

# arr = [100000 for _ in range(n + 1)]
# arr[n] = 0
# cnt = n
# while True:
#     if cnt <= 1:
#         break

#     arr[cnt - 1] = arr[cnt] + 1
#     cnt -= 1

#     if cnt % 3 == 0:
#         arr[cnt//3] = min(arr[cnt//3], arr[cnt] + 1)
#         cnt = cnt // 3

#     elif cnt % 2 == 0:
#         arr[cnt//2] = min(arr[cnt//2], arr[cnt] + 1)
#         cnt = cnt // 2
        

# print(arr[1])

arr = [0 for _ in range(n+1)]

for i in range(2, n + 1):
    arr[i] = arr[i-1] + 1
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)

print(arr[n])
