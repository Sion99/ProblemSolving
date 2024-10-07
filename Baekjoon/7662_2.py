# 이중 우선순위 큐

# 우선순위 큐처럼 데이터 삽입, 삭제
# 데이터 삭제할 때 연산 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 삭제
# 총 두가지 연산 -> 데이터 삽입, 삭제
# 삭제 두가지 방법 -> 우선순위 높은 것 삭제, 낮은 것 삭제

# 큐에 저장된 각 정수의 값 자체가 우선순위

# Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 최대 최소 출력

import sys
import heapq

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    # k가 최대 백만이기 때문에 O(N^2)는 불가능
    # 우선순위 큐를 2개 둬야할 듯
    maxheap = []
    minheap = []
    for i in range(k):
        order, n = input().rstrip().split()
        n = int(n)
        # 동일한 정수가 삽입될 수 있음
        # D 1 -> Q에서 최댓값 삭제
        # D -1 -> Q에서 최솟값 삭제
        # I n -> Q에 n 삽입

        if order == 'I':
            # 최대 힙은 부호 바꿔서 넣으랬는데
            heapq.heappush(maxheap, -n)
            heapq.heappush(minheap, n)
        if order == 'D':
            if n == -1 and minheap:
                # 최댓값 삭제 -> 최대 힙에서 OUT?
                maxheap.remove(-1*heapq.heappop(minheap))
            elif n == 1 and maxheap:
                # 최솟값 삭제
                minheap.remove(-1*heapq.heappop(maxheap))
        
    if not maxheap or not minheap:
        print('EMPTY')
    else:
        min, max = heapq.heappop(minheap), -1*heapq.heappop(maxheap)
        print(max, min)
