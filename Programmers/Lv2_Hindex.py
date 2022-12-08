# 12/08
# H-Index의 개념을 잘 이해하지 못해서 너무 어렵게 풀었다
# 분발하자..
# 1시간 넘게 걸린듯..?

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    citations.insert(0, 0)
    print(citations)
    for i in range(1, len(citations)):
        print(i)
        if citations[i] >= i:
            answer = i
        else:
            break
    return answer


citations = [5, 3, 3, 8, 10]
print(solution(citations))
