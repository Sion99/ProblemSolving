from collections import deque


def solution(s):
    answer = 0
    deq = deque(s)

    while (len(deq) != 0):
        answer += 1
        first = deq.popleft()
        firstn = 1
        others = 0
        for i in range(len(deq)):
            if deq.popleft() == first:
                firstn += 1
            else:
                others += 1
            if firstn == others:
                break

    return answer
