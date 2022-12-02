def solution(brown, yellow):
    # 제일 큰 직사각형에서
    # yellow 직사각형을 빼면 brown이 남음
    # 제일 큰 직사각형  x = yellow + brown
    answer = []
    x = brown + yellow

    # x가 a*b라면 yellow는 (a-2)*(b-2)
    # brown은 a*b - (a-2) * (b-2)
    # 조건에 따라, a >= b >= 3
    array = []
    for i in range(3, x+1):
        if x % i == 0:
            array.append(i)

    for i in array:
        result = 0
        for j in array:
            if (i+j) == ((brown)/2 + 2):
                if (i-2)*(j-2) == yellow:
                    answer = [j, i]
                    result = 1
                    break

        if result == 1:
            break

    return answer
