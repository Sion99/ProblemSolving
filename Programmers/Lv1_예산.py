def solution(d, budget):
    answer = 0
    d.sort()
    temp = 0
    count = 0
    for i in d:
        count += 1
        temp += i
        if temp > budget:
            count -= 1
            break
    answer = count
    return answer
