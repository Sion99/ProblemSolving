def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i < len(completion):
            a = i
        if participant[i] != completion[a]:
            # 똑같은 인덱스에 값이 없다 -> 완주를 못함
            answer = participant[i]
            break

    return answer
