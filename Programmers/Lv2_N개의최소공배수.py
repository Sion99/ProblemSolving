
def solution(arr):
    answer = 0
    arr.sort()

    # 두 숫자끼리 최소공배수를 구해보자
    temp = arr[0]
    for i in range(len(arr)):
        for j in range(max(arr[i], temp), arr[i]*temp+1):
            if j % arr[i] == 0 and j % temp == 0:
                temp = j
                break
    answer = temp

    return answer
