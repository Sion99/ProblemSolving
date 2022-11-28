def solution(nums):
    answer = 0
    half = len(nums)/2
    # 먼저 배열을 정렬해보자
    # nums.sort()
    # 배열의 중복값을 없애자
    nums = list(set(nums))
    if len(nums) >= half:
        answer = half
    else:
        answer = len(nums)

    return answer
