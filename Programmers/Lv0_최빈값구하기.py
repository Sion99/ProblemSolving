# 12/01
# 은근히 애를 많이 먹었던 문제
# 최빈값이 여러개면 -1을 출력하게끔 추가적으로 처리해야 한다.


def solution(array):
    frequency = []
    temp = list(set(array))
    for i in temp:
        frequency.append([i, array.count(i)])

    frequency.sort(key=lambda x: (x[1], x[0]))
    max = frequency.pop()
    answer = max[0]

    for i in range(len(frequency)):
        if frequency[i][1] == max[1]:
            answer = -1
            break

    return answer
