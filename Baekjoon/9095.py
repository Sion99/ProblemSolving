# 1, 2, 3 더하기

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수

t = int(input())
arr = [1, 2, 4]

for i in range(3, 11):
    arr.append(arr[i-3] + arr[i-2] + arr[i-1])

for _ in range(t):
    n = int(input())
    print(arr[n-1])