# RGB 거리

# 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함
# 1. 1번 집의 색은 2번 집의 색과 같지 않아야 함
# 2. N번 집의 색은 N-1번 집의 색과 같지 않아야 함
# 3. i번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 함

n = int(input())
red = []
green = []
blue = []

rgbs = [[0] * 3 for _ in range(n)]
for i in range(n):
    r, g, b = map(int, input().split())
    rgbs[i][0] = r
    rgbs[i][1] = g
    rgbs[i][2] = b

arr = [[0] * 3 for _ in range(n)]

arr[0][0] = rgbs[0][0]
arr[0][1] = rgbs[0][1]
arr[0][2] = rgbs[0][2]

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + rgbs[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + rgbs[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + rgbs[i][2]

print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))