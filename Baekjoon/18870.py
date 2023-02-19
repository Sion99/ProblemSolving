import copy

n = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in arr:
    dic[i] = 0

newarr = copy.deepcopy(arr)
arr = list(set(arr))
arr.sort()

for i in range(len(arr)):
    dic[arr[i]] = i

for i in newarr:
    print(dic[i], end=' ')
