def solution(food):
    arr = ''
    answer = ''
    for i in range(1, len(food)):
        howmany = (food[i]//2)
        if howmany >= 1:
            for j in range(howmany):
                arr += str(i)
    answer = arr + str(0) + ''.join(reversed(arr))
    return answer


food = [1, 3, 4, 6]
print(solution(food))

# 정답!
