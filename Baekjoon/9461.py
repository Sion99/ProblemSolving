# 파도반 수열
# DP 문제
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12 ...

# 규칙은 1 1 1 2 2 부터는 arr[i] = arr[i-1] + arr[i-5]

t = int(input())

arr = [1, 1, 1, 2, 2]

for i in range(5, 101):
    arr.append(arr[i - 1] + arr[i - 5])

for _ in range(t):
    n = int(input())
    print(arr[n - 1])
    