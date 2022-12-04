def solution(s):
    answer = -1
    while (True):
        result = 0
        temp = ''
        for i in range(len(s)):
            if i == len(s)-2:
                break
            if s[i] == s[i+1]:
                result = 1
                if (i < len(s)-2):
                    temp += s[i+2:]
                    break
                else:
                    break
            else:
                temp += s[i]
                print(temp)
        s = temp
        if result == 0:
            answer = 0
            break
    print(s)
    if len(s) == 0:
        answer = 1
    return answer


s = 'baabaa'
print(solution(s))
