# 총 소요시간 3시간 정도
# 푸는 방식은 금방 나왔는데, 테스트 케이스 중 2개가 시간 초과가 되어서
# 시간 단축 어떻게든 해보겠다고 엄청나게 시간을 많이 잡아먹었다..
# 머리 터질 거 같음


def solution(id_list, report, k):
    answer = []
    user = []
    mailed = []
    reported = []
    banned = []

    # answer 0으로 초기화
    for i in range(len(id_list)):
        answer.append(0)

    for i in range(len(report)):
        case = report[i].split(' ')
        user.append([case[0], case[1]])

    # 신고에 중복 제거
    user = set(list(map(tuple, user)))
    user = list(user)

    for i in range(len(user)):
        reported.append(user[i][1])

    for i in range(len(id_list)):
        if reported.count(id_list[i]) >= k:
            banned.append(id_list[i])

    for i in range(len(user)):
        if user[i][1] in banned:
            mailed.append(user[i][0])

    for i in range(len(mailed)):
        for j in range(len(id_list)):
            if id_list[j] == mailed[i]:
                answer[j] += 1

    return answer
