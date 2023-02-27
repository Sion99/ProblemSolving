n, m = map(int, input().split())

ans = 1
for i in range(n - m + 1):
    ans *= n - i

div = 1
for i in range(1, m + 1):
    div *= i

print(ans // div)
