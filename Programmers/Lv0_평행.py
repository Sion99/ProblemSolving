def solution(dots):
    # 모든 직선의 기울기 slope를 찾는다
    slope = []
    for i in range(len(dots)-1):
        for j in range(i+1, len(dots)):
            temp = (dots[j][0] - dots[i][0])/(dots[j][1] - dots[i][1])
            slope.append(temp)

    answer = 0
    for i in slope:
        if slope.count(i) > 1:
            answer = 1
            break

    return answer
