# 12/11 programmers
# 순열로 하니까 안풀리네.. 머지
# 순열로 하니까 n=12 만 되어도 느려 터짐
# n=20으로 하니까 아예 먹통
# 이 방법으로 푸는 거 아니네..
# 아직 못 품

from itertools import permutations


def solution(n):
    answer = 1
    case = []
    for i in range(n):
        case.append(1)

    while (True):
        if case.count(1) > 1:
            case = case[2:]
            case.append(2)
            per = list(set(permutations(case, len(case))))
            answer += len(per)
        else:
            break
    return answer


print(solution(4))
