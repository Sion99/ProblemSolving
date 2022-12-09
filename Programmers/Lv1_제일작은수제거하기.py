def solution(arr):
    answer = []
    for i in arr:
        answer.append(i)
    arr.sort()
    index = answer.index(arr[0])
    answer.pop(index)
    if len(answer) == 0:
        answer.append(-1)
    return answer
