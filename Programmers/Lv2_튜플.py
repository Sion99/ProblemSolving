# 12/22
# 딕셔너리와 점점 친해지는 중..
# 앞으로 더 친해지자 우리 ^_____^

def solution(s):
    array = []
    answer = []
    specialchars = '{}'
    arr = s.split(',')
    for i in range(len(arr)):
        temp = ''
        for j in range(len(arr[i])):
            if arr[i][j] != '{' and arr[i][j] != '}':
                temp += arr[i][j]
        array.append(int(temp))
    # 개수 별로 줄 세우기
    dic = {}
    temp = list(set(array))
    for i in temp:
        dic[array.count(i)] = i
    keylist = list(dic.keys())
    keylist.sort(reverse=True)
    for i in keylist:
        answer.append(dic[i])
    return answer
