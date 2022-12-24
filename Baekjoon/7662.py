# 이중 우선순위 큐
# Gold 4
# 큐 두개를 만들어보자

import sys
from heapq import *
# def mininsert(heap, num):
#     heap.append(num)
#     index = len(heap)-1
#     while ((index != 1) and (num < heap[index//2])):
#         heap[index], heap[index//2] = heap[index//2], heap[index]
#         index = index//2


# def maxinsert(heap, num):
#     heap.append(num)
#     index = len(heap)-1
#     while ((index != 1) and (num > heap[index//2])):
#         heap[index], heap[index//2] = heap[index//2], heap[index]
#         index = index//2


# def mindelete(heap, num):
#     result = heap[1]
#     heap[-1], heap[1] = heap[1], heap[-1]
#     heap.pop()
#     parent = 1
#     while (True):
#         child = parent*2
#         if (child+1 < len(heap) and heap[child] > heap[child] + 1):
#             child += 1
#         if (child >= len(heap) or heap[child] > heap[parent]):
#             break
#         heap[child], heap[parent] = heap[parent], heap[child]
#         parent = child

#     return result


# def maxdelete(heap, num):
#     result = heap[1]
#     heap[-1], heap[1] = heap[1], heap[-1]
#     heap.pop()
#     parent = 1
#     while (True):
#         child = parent*2
#         if (child+1 < len(heap) and heap[child] < heap[child] + 1):
#             child += 1
#         if (child >= len(heap) or heap[child] < heap[parent]):
#             break
#         heap[child], heap[parent] = heap[parent], heap[child]
#         parent = child

#     return result


# t = int(sys.stdin.readline().rstrip())
# for i in range(t):
#     maxheap = [0]
#     minheap = [0]
#     k = int(sys.stdin.readline().rstrip())
#     for j in range(k):
#         order = sys.stdin.readline().rstrip().split(' ')
#         # print(order)
#         if order[0] == 'I':
#             mininsert(minheap, int(order[1]))
#             maxinsert(maxheap, int(order[1])*-1)
#         elif order[0] == 'D':
#             if order[1] == '-1' and minheap:
#                 mindelete(minheap)
#             elif order[1] == '1' and maxheap:
#                 maxdelete(maxheap)

#     if len(deq) == 0:
#         print('EMPTY')
#     else:
#         temp = list(deq)
#         temp.sort()
#         deq = deque(temp)
#         min = deq.popleft()
#         max = deq.pop()
#         print(max, min)

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    k = int(sys.stdin.readline().rstrip())
    minheap = []
    maxheap = []
    for j in range(k):
        order = sys.stdin.readline().rstrip().split(' ')
        # print(order)
        if order[0] == 'I':
            value = int(order[1])
            heappush(minheap, value)
            heappush(maxheap, -value)
        elif order[0] == 'D':
            if order[1] == '-1' and minheap:
                maxheap.pop(-1*heappop(minheap))
            elif order[1] == '1' and maxheap:
                minheap.pop(heappop(maxheap)*-1)
    if len(minheap) == 0 or len(maxheap) == 0:
        print('EMPTY')
    else:
        min = heappop(minheap)
        max = heappop(maxheap)*-1
        print(max, min)
