# 12/18 programmers
# 5분컷 쉽다 ㅎㅎ..

from collections import deque


def solution(priorities, location):
    answer = 0
    deq = deque([])
    for i in range(len(priorities)):
        deq.append([i, priorities[i]])
    while (True):
        check = deq.popleft()
        result = 0
        for i in range(len(deq)):
            if deq[i][1] > check[1]:
                result = 1
                break
        if result == 1:
            deq.append(check)
        else:
            answer += 1
            if check[0] == location:
                break
    return answer
