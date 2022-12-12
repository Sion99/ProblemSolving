# 12/09
# 실버 3 11441 합구하기

n = int(input())
m = []
for i in range(n):
    temp = map(int, input().split())
    m.append(temp)
a = int(input())
for i in range(a):
    i, j = map(int, input().split())
    print(i, j)
