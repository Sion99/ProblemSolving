# 12/05
# 첫 시도부터 정답까지 며칠 걸림..
# 답은 스택!

def solution(s):
    answer = 0
    s = list(s)
    last = len(s)
    while (True):
        stack = []
        for i in s:
            if len(stack) > 0:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        s = stack
        if len(s) == 0:
            answer = 1
            break
        if last == len(s):
            answer = 0
            break
        last = len(s)
    return answer
