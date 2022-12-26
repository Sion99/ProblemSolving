# 12/23 도전중
# 이게 아닌가ㅏ벼..
# 가장 ~한 수는 heap을 쓰는 거라는 것을 바로 떠올려야 한단다!
# 다시 도전해보기

# 12/26 해결완료!
# heap 쓰니까 바로 되네
from heapq import *


def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heappush(heap, -i)
    print(heap)
    while (n > 0):
        max = abs(heappop(heap))
        if max == 0:
            return 0
        max -= 1
        n -= 1
        heappush(heap, -max)
    for i in heap:
        answer += i*i

    return answer

    # def solution(n, works):
    #     answer = 0
    #     works.sort(reverse=True)
    #     i = 1
    #     n -= 1
    #     works[0] -= 1
    #     while (n > 0):
    #         if i >= len(works):
    #             i = i % len(works)
    #         if i != len(works)-1 and works[i] > works[i+1]:
    #             while (True):
    #                 if works[i] == works[i+1]:
    #                     break
    #                 works[i] -= 1
    #                 n -= 1
    #         else:
    #             works[i] -= 1
    #             n -= 1
    #             i += 1

    #     print(works)

    #     for j in works:
    #         answer += j*j
    #     return answer

    works = [4, 3, 3]
    n = 4
    works = [800, 100, 55, 45]
    n = 999
    print(solution(n, works))
