def solution(n):
    answer = 0
    nextn = n
    a = str(bin(n)[2:]).count('1')
    while (True):
        nextn += 1
        b = str(bin(nextn)[2:]).count('1')
        if a == b:
            break
    answer = nextn
    return answer
