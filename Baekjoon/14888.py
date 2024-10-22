# 실버 1 14888. 연산자 끼워넣기

# N개로 이루어진 수열
# 수와 수 사이에 끼워넣을 수 있는 N-1개 연산자
# +, -, x, % 이루어짐

# 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만들 수 있다.
# 단 수의 순서를 바꾸면 안된다

# 식의 계산은 연산자 우선 순위 무시하고 앞에서부터 진행
# 나눗셈은 몫만 취함

# 음수를 양수로 나눌 때는, 양수로 바꾸고 계산한 다음, 몫을 음수로 바꾼다.

# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 최대 최소

import copy

def backtrack(operations, selected, m):
    global equations
    if len(selected) == m:
        temp = copy.deepcopy(selected)
        # 연산자 n-1개 골랐으면
        equations.append(temp)
    else:
        for i in range(m):
            # 중복은 안돼요!
            selected.append(operations[i])
            backtrack(operations, selected, m)
            selected.pop()



n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

operations = []
for i in range(len(op)):
    for j in range(op[i]):
        operations.append(i)
print(operations)

equations = []
backtrack(operations, [], n-1)
print(equations)

mx = -2**31
mn = 2**31

for equation in equations:
    arr[]
