def solution(array, n):
    answer = 0
    array.sort()
    print(array)
    diff = 999
    min = 0
    for i in range(len(array)):
        if abs(n-array[i]) < diff:
            diff = abs(n-array[i])
            min = array[i]

    answer = min
    return answer
