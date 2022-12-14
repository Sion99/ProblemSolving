def solution(arr1, arr2):
    print(len(arr1), len(arr2[0]))
    arr = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    print(arr)

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            multiplied = 0
            for k in range(len(arr1[0])):
                multiplied += arr1[i][k] * arr2[k][j]
            arr[i][j] = multiplied

    return arr


# arr1 = [[2, 3, 2],
#         [4, 2, 4],
#         [3, 1, 4]]
arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[5, 4, 3],
#         [2, 4, 1],
#         [3, 1, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))
