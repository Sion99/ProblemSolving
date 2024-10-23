# 골드 5 1759. 암호 만들기

# 암호는 서로 다른 L개의 알파벳 소문자로 구성되며 최소 한 개의 모음과 최소 두 개의 자음으로 구성됨
# 알파벳이 증가하는 순서로 배열되어 있다
# 문자의 종류는 C가지
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하라

answer = set()

def backtrack(arr, selected, l, c, start):
    global answer
    if len(selected) == l:
        if is_valid(selected):
            answer.add(tuple(selected))
    else:
        for i in range(start, c):
            selected.append(arr[i])
            backtrack(arr, selected, l, c, i+1)
            selected.pop()

l, c = map(int, input().split())
arr = list(input().split())

# 암호는 알파벳 오름차순으로 배열되어 있어야 하고
# 중복되는 문자는 존재하지 않는다

arr.sort()

vowels = ['a', 'e', 'i', 'o', 'u']

# 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있는지?
def is_valid(passwd):
    # 모음 세기
    v_cnt = 0
    c_cnt = 0
    for c in passwd:
        if c in vowels:
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt >= 1 and c_cnt >= 2:
        return True
    return False

backtrack(arr, [], l, c, 0)

answer = sorted(answer)

for a in answer:
    for i in a:
        print(i, end='')
    print()