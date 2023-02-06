n, m = map(int, input().split())

dic = {}
for i in range(0, n):
    str = input().split()
    dic[str[0]] = str[1]

for i in range(0, m):
    query = input()
    print(dic[query])
