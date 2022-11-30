def solution(s):
    answer = True
    open = []
    for i in s:
        if i == '(':
            open.append(i)
        else:
            # 여는 괄호가 나온 적 있다면
            if not open:
                answer = False
                break
            else:
                open.pop()

    if open:
        answer = False

    return answer
