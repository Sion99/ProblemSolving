# 11/30
# 코드가 너무 지저분하다..
# 먼가 더 잘 만들 수 있는데 지저분하게 만든 느낌
# 나중에 다듬어야지

def solution(n, words):
    turns = [0 for i in range(n)]
    fail = 0
    result = 0
    already = []
    already.append(words[0])
    latest = words[0][-1]
    turns[0] += 1
    i = 0
    while (i < len(words)-1):
        i += 1
        turns[i % n] += 1
        if words[i].startswith(latest):
            if words[i] in already:
                fail = i % n
                result = 1
                break
            else:
                already.append(words[i])
                latest = words[i][-1]
        else:
            fail = i % n
            result = 1
            break

    if result == 0:
        answer = [0, 0]
    else:
        answer = [fail+1, turns[fail]]

    return answer
