# deque로 하는데 왜 안풀리지
# 코드가 너무 더러운듯..
# 아래꺼로 하니까 잘됨

from collections import deque


# def solution(people, limit):
#     answer = 0
#     people.sort()
#     deq = deque(people)
#     temp = 0
#     boat = 1
#     print(deq)
#     small = deq.popleft()
#     if small > limit/2:
#         return len(deq)
#     elif small == limit/2:
#         return len(people)-(people.count(small)//2)
#     else:
#         big = deq.pop()
#         while (len(deq) != 0):
#             print(small, big)
#             if small + big < limit:
#                 temp += (small + big)
#                 small = deq.popleft()
#             elif small + big == limit:
#                 boat += 1
#                 temp = 0
#                 if len(deq) > 0:
#                     small = deq.popleft()
#                 if len(deq) > 0:
#                     big = deq.pop()
#             else:
#                 boat += 1
#                 big = deq.pop()

#         if len(deq) == 1:
#             last = deq.pop()
#         else:
#             last = 0

#         if temp + last <= limit:
#             boat += 1
#         else:
#             boat += 2

#         return boat


def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    boat = 0
    while deq:
        temp = limit - deq.pop()
        while deq and deq[0] <= temp:
            temp -= deq.popleft()
        boat += 1
    answer = boat
    return answer


people = [70, 50, 80, 50, 49, 48, 51]
# people = [10, 20, 30, 40, 50, 60, 90, 91, 92, 93, 94, 95, 99]
limit = 100
print(solution(people, limit))
