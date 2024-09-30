# 2xn 타일링 2

# 2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수
# n = 1 -> 1
# n = 2 -> 3
# n = 3 -> 5
# n = 4 -> 11

# a(i) = a(i-2) * 2 + a(i-1)

n = int(input())

arr = [1, 3]

for i in range(2, n):
    arr.append((arr[i-2] * 2 + arr[i-1]) % 10007)

print(arr[n-1])