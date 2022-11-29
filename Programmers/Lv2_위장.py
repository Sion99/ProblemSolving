# 11/29 21:00-
# 생각보다 많이 어려운데? 22:23 까지 못품..

from itertools import combinations


def solution(clothes):
    answer = 0
    # 매일 다른 옷을 조합하여 입기
    # clothes는 옷에 대한 2차원 배열 [이름, 종류]
    # 서로 다른 옷의 조합의 수를 return
    # 같은 이름의 의상은 존재하지 않음

    ctype = []

    for i in clothes:
        ctype.append(i[1])

    sum = 0
    sum += len(ctype)
    # sum += len(ctype)-1
    if len(ctype) <= 1:
        answer = len(ctype)
    elif len(ctype) == 2:
        answer = len(ctype)+1
    for i in range(2, len(ctype)/2):
        temp = list(set(list(combinations(ctype, i))))
        temp2 = len(temp)

        # for j in range(len(temp)):
        #     if temp.count(temp[j]) != 1:
        #         temp2 = temp2 - 1

        print(temp)
        print(temp2)
        sum += temp2

    answer = sum
    return answer


def solution(clothes):
    answer = 0
    # 매일 다른 옷을 조합하여 입기
    # clothes는 옷에 대한 2차원 배열 [이름, 종류]
    # 서로 다른 옷의 조합의 수를 return
    # 같은 이름의 의상은 존재하지 않음

    ctype = []

    for i in clothes:
        ctype.append(i[1])

    sum = 0
    # 겹치지 않을 때
    if len(ctype) == len(set(ctype)):
        for i in range(1, len(ctype)):
            temp = list(combinations(ctype, i))
            sum += len(temp)

    # 겹칠때
    else:
        sum += len(ctype)
        ttype = set(ctype)
        k = 1
        while (True):
            k += 1
            temp2 = set(list(combinations(ttype, i)))
            print(temp2)
            if k >= len(ttype):
                break

    answer = sum
    return answer
