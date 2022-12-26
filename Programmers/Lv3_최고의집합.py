# 12/26
# 최고의 집합
# 뭔가 계속 걸리적거리네..

def solution(n, s):
    # 몇 개의 자연수를 쓸 건지 n도 정말 중요하다!
    answer = []
    if n > s:
        return [-1]
    if s % n == 0:
        for i in range(n):
            answer.append(s//n)
    else:
        temp = s - s % n
        for i in range(n):
            answer.append(temp//n)
        for i in range(s % n):
            answer[i] += 1
    answer.sort()
    return answer
