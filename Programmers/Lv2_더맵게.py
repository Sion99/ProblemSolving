# 12/27

from heapq import *


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while (True):
        least = heappop(scoville)
        if least >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heappop(scoville)
        heappush(scoville, least + second*2)
        answer += 1
    return answer
