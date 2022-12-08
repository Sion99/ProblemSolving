# 12/08 programmers
# 진짜 더럽게 풀었다.. ㅠㅠ

def calc(s):
    arr = [0, 0, 0]
    last = [0]
    result = 1
    for i in s:
        if i == '(':
            arr[0] += 1
            last.append(1)
        elif i == ')':
            if last[-1] != 1:
                result = 0
                break
            if arr[0] == 0:
                result = 0
                break
            arr[0] -= 1
            last.pop()
        elif i == '[':
            arr[1] += 1
            last.append(2)
        elif i == ']':
            if last[-1] != 2:
                result = 0
                break
            if arr[1] == 0:
                result = 0
                break
            arr[1] -= 1
            last.pop()
        elif i == '{':
            last.append(3)
            arr[2] += 1
        else:
            if last[-1] != 3:
                result = 0
                break
            if arr[2] == 0:
                result = 0
                break
            arr[2] -= 1
            last.pop()
    for i in arr:
        if i != 0:
            result = 0
            break

    return result


def solution(s):
    every = [s]
    answer = 0
    for i in range(1, len(s)):
        temp = s[i:] + s[:i]
        every.append(temp)
    for i in every:
        answer += calc(i)

    return answer
