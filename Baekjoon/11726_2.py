# 2xn 타일링

# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8 ...

arr = [1, 2]

n = int(input())

for i in range(2, n):
    arr.append((arr[i-2] + arr[i-1])%10007)

print(arr[n-1])