def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    i = 1
    n -= 1
    works[0] -= 1
    while (n > 0):
        if i >= len(works):
            i = i % len(works)
        if i != len(works)-1 and works[i] > works[i+1]:
            while (True):
                if works[i] == works[i+1]:
                    break
                works[i] -= 1
                n -= 1
        else:
            works[i] -= 1
            n -= 1
            i += 1

    print(works)

    for j in works:
        answer += j*j
    return answer


works = [4, 3, 3]
n = 4
works = [800, 100, 55, 45]
n = 999
print(solution(n, works))
