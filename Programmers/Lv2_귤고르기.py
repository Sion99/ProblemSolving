# 12/30
# 내가 생각해도 극혐인 시간복잡도..
# 82.4 점이다 ㅠㅠ
# 시간복잡도 개선을 해야할 듯.. 시간초과남

def solution(k, tangerine):
    answer = 0
    unique = list(set(tangerine))
    dic = {}
    for i in unique:
        dic[i] = tangerine.count(i)
    temp = []
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    i = 0
    count = 0
    while (True):
        if len(temp) == k:
            break
        temp.append(dic[i][0])
        count += 1
        if count == dic[i][1]:
            count = 0
            i += 1
    answer = len(list(set(temp)))
    return answer
