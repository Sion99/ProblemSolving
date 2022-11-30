def solution(x, n):
    answer = []
    interval = x
    for i in range(n):
        answer.append(interval)
        interval += x
    return answer