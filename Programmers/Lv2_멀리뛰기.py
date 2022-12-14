# 12/11 programmers
# 순열로 하니까 안풀리네.. 머지
# 순열로 하니까 n=12 만 되어도 느려 터짐
# n=20으로 하니까 아예 먹통
# 이 방법으로 푸는 거 아니네..
# 아직 못 품

# 12/14
# 방금 손으로 해보니까 뭔가 피보나치 같음
# 1 -> 1, 2 -> 2, 3 -> 3, 4 -> 5, 5 -> 8, 6 -> 13 ...
# 진짜 어이없네 ㅠㅠ
# 내 순열...

def solution(n):
    answer = 0
    fib = [0, 1]
    for i in range(2, n+2):
        fib.append(fib[i-2]+fib[i-1])
    answer = fib[-1] % 1234567
    return answer

# from itertools import permutations

# def solution(n):
#     answer = 1
#     case = []
#     for i in range(n):
#         case.append(1)

#     while (True):
#         if case.count(1) > 1:
#             case = case[2:]
#             case.append(2)
#             per = list(set(permutations(case, len(case))))
#             answer += len(per)
#         else:
#             break
#     return answer


print(solution(4))
