def solution(s):
    answer = ''

    arr = s.split(' ')
    number = []
    for i in range(len(arr)):
        number.append(int(arr[i]))

    number.sort()
    answer += str(number[0])
    answer += ' '
    answer += str(number[-1])

    return answer
