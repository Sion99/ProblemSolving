
def solution(ingredient):
    stack = []
    answer = 0
    waiting = 0
    for i in range(len(ingredient)-2):
        if ingredient[i] == 1:
            if waiting == 1:
                stack.pop()
                waiting = 0
                answer += 1
            # 괄호 여는 식
            stack.append(1)
        if ingredient[i] == 2 and ingredient[i+1] == 3:
            if stack[-1] == 1 and ingredient[i+2] == 1:
                stack.pop()
                answer += 1
            elif stack[-1] == 1 and ingredient[i+2] != 1:
                waiting = 1

    return answer

# 12/12
# 위처럼 하니까 시간초과났음
# 이렇게 풀어야 한다!


def solution(ingredient):
    stack = []
    answer = 0
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) > 3:
            if stack[-4:] == [1, 2, 3, 1]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1

    return answer


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))
