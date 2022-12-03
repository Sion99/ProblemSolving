def solution(arr):
    answer = []
    temp = arr[0]
    for i in range(1, len(arr)):
        if i == len(arr)-1:
            answer.append(temp)
            if temp == arr[i]:
                continue
            else:
                answer.append(arr[i])
        else:
            if temp == arr[i]:
                continue
            else:
                answer.append(temp)
                temp = arr[i]

    return answer
