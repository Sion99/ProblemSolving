# 신나는 함수 실행

# 재귀함수 w(a, b, c)가 있음
# a <= 0 or b <= 0 or c <= 0 -> 1
# a > 20 or b > 20 or c > 20 -> w(20, 20, 20)
# a < b and b < c -> w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# 나머지는 -> w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

arr = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                arr[i][j][k] = 1
                continue
            if i < j and j < k:
                arr[i][j][k] = arr[i][j][k - 1] + arr[i][j - 1][k - 1] - arr[i][j - 1][k]
            else:
                arr[i][j][k] = arr[i - 1][j][k] + arr[i - 1][j - 1][k] + arr[i - 1][j][k - 1] - arr[i - 1][j - 1][k - 1]


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        target = 1
    elif a > 20 or b > 20 or c > 20:
        target = arr[20][20][20]
    else:
        target = arr[a][b][c]
    print(f"w({a}, {b}, {c}) = {target}")