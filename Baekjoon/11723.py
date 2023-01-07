import sys

# 시간 초과가 뜨네..


# m = int(sys.stdin.readline().rstrip())
# dic = {}
# for i in range(1, 21):
#     dic[str(i)] = 0

# for i in range(m):
#     order = (sys.stdin.readline().rstrip())
#     order = order.split(' ')
#     if order[0] == 'add':
#         dic[order[1]] = 1
#     elif order[0] == 'remove':
#         if dic[order[1]] == 1:
#             dic[order[1]] = 0
#     elif order[0] == 'check':
#         if dic[order[1]] == 1:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 'toggle':
#         if dic[order[1]] == 1:
#             dic[order[1]] = 0
#         else:
#             dic[order[1]] = 1
#     elif order[0] == 'all':
#         for j in range(1, 21):
#             dic[str(j)] = 1
#     elif order[0] == 'empty':
#         for j in range(1, 21):
#             dic[str(j)] = 0


m = int(sys.stdin.readline().rstrip())
arr = set([])
for i in range(m):
    order = (sys.stdin.readline().rstrip()).split(' ')
    if order[0] == 'add':
        arr.add(int(order[1]))
    elif order[0] == 'remove':
        if list(arr).count(int(order[1])) == 1:
            arr.remove(int(order[1]))
    elif order[0] == 'check':
        if list(arr).count(int(order[1])) == 1:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if list(arr).count(int(order[1])) == 1:
            arr.remove(int(order[1]))
        else:
            arr.add(int(order[1]))
    elif order[0] == 'all':
        arr = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                  12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif order[0] == 'empty':
        arr = set([])
