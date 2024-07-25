def to_postfix(equation):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = []

    for token in equation:
        if token.isalpha():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and priority.get(stack[-1], 0) >= priority[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


equation = input()
postfix = to_postfix(equation)
print(postfix)