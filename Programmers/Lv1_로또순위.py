def check(count):
    if count == 2:
        return 5
    elif count == 3:
        return 4
    elif count == 4:
        return 3
    elif count == 5:
        return 2
    elif count == 6:
        return 1
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    count = 0
    zeros = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeros += 1

    for i in range(len(win_nums)):
        if win_nums[i] in lottos:
            count += 1

    min = check(count)
    max = check(count+zeros)
    answer.append(max)
    answer.append(min)

    return answer
