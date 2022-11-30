def solution(s):
    answer = ''
    string = s.split(' ')
    for i in range(len(string)):
        if i != 0:
            answer += ' '
        if len(string[i]) != 0:
            temp = string[i].lower()
            first = temp[0].upper()
            answer += first
            answer += temp[1:]
        print(answer)

    return answer
