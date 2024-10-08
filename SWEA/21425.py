# 21425. +=

# 현재 값에서 += 연산을 원하는 순서대로 원하는 만큼 수행하여 N 초과가 되게 하라

t = int(input())

for i in range(1, t+1):
    a, b, n = map(int, input().split())
    # 번갈아 가면서 하는게 베스트
    cnt = 0
    while a <= n or b <= n:
        if a < b:
            a += b
        else:
            b += a
        cnt += 1
        if a > n or b > n:
            break
    print(cnt)