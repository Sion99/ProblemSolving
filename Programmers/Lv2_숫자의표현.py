# 11/30
# 개어려운데??
# 30분 동안 곰곰히 생각해봐도 전혀 모르겠다..
# 이게 어떻게 73% 짜리..
# 진짜 너무 어려움

def solution(n):
    i = n
    count = 1
    while (True):
        if i % 2 == 0:
            i = i//2
        else:
            break
    # 약수 구하기
    for j in range(1, i):
        if i % j == 0:
            count += 1
    answer = count

    return answer
