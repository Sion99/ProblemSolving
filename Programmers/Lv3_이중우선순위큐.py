# 12/15
# 레벨 3도 건들기 시작
# 딱대

from collections import deque


def solution(operations):
    answer = []
    deq = deque()
    for i in operations:
        op = i.split()
        # 삽입할 때가 가장 중요함. 인덱스가 0에 가까울 수록 작은 값이,
        # 인덱스가 끝 쪽일 수록 큰 값이 나와야 함
        if op[0] == 'I':
            deq.append(int(op[1]))
            temp = list(deq)
            temp.sort()
            deq = deque(temp)
        elif op[0] == 'D':
            if len(deq) != 0:
                if op[1] == '1':
                    deq.pop()
                else:
                    deq.popleft()
    if len(deq) == 0:
        answer = [0, 0]
    else:
        answer = [deq.pop(), deq.popleft()]

    return answer
