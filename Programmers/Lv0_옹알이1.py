# 12/01
# 절대 Lv0 문제 아님.. ㅋㅋㅋㅋ
# Lv0인데 정답률이 24%밖에 안된다

from itertools import permutations


def solution(babbling):
    reference = ['aya', 'ye', 'woo', 'ma']
    every = []
    for i in range(2, 5):
        temp = list(permutations(reference, i))
        for j in temp:
            temp2 = ''
            for k in range(i):
                temp2 += j[k]
            every.append(temp2)

    every = list(set(every))
    every += reference
    answer = 0
    for i in babbling:
        if i in every:
            answer += 1

    return answer
