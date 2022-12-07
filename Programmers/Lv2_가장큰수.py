# 12/06
# itertools permutations으로 푸는 것은 아닌듯하다..


def solution(numbers):
    changed = []
    for i in numbers:
        changed.append(str(i))
    answer = ''
    changed.sort()
    print(changed)
    changed.sort(reverse=True)
    print(changed)

    for i in changed:
        answer += i

    return answer
