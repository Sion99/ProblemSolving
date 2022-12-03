# 12/03

def solution(progresses, speeds):
    answer = []
    day = 0
    patch = 0
    while (len(progresses) > 0):
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            patch += 1
            continue
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        day += 1
        answer.append(patch)
        patch = 0
    answer.append(patch)
    answer = [i for i in answer if i != 0]

    return answer
