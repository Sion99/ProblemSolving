import logging

# 로그 설정
logging.basicConfig(level=logging.INFO)


def rotate_90(arr):
    logging.info("Applying 90 degree rotation")
    return list(map(list, zip(*arr[::-1])))


def rotate_multiple(arr, times):
    rotated_arr = arr
    for i in range(times):
        rotated_arr = rotate_90(rotated_arr)
        logging.info(f"After {90 * (i + 1)} degree rotation: {rotated_arr}")
    return rotated_arr

# 배열 출력 함수


def print_array(arr, description):
    print(f"\n{description}")
    for row in arr:
        print(" ".join(map(str, row)))


# 초기 배열
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

# 시계 방향 90도 회전
arr_90 = rotate_multiple(arr, 1)
print_array(arr_90, "90도 회전")

# 시계 방향 180도 회전 (90도 2번 적용)
arr_180 = rotate_multiple(arr, 2)
print_array(arr_180, "180도 회전")

# 시계 방향 270도 회전 (90도 3번 적용)
arr_270 = rotate_multiple(arr, 3)
print_array(arr_270, "270도 회전")

# 시계 방향 360도 회전 (90도 4번 적용, 원상 복귀)
arr_360 = rotate_multiple(arr, 4)
print_array(arr_360, "360도 회전 (원상 복귀)")
