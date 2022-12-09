# 12/09
# 너무 어려워
# 몇번을 틀리고 고친지 모르겠다..
# 아직 못 품 ㅠㅠ

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i % n)+1)
    return answer


def solution(n, left, right):
    answer = []
    a = (left+1)//n
    b = (right+1)//n + 1
    c = right-left + 1
    newleft = left % n
    for i in range(a, b+1):
        for j in range(i):
            answer.append(i)
        if i == 0:
            continue

        for j in range(i+1, n+1):
            answer.append(j)

    answer = answer[newleft:]
    return answer[0:c]


# print(solution(13, 90, 99))
print(solution(4, 0, 15))
print(solution(5, 1, 10))
print(solution(4, 7, 14))
print(solution(3, 2, 5))
