# 11/30
# 이진법으로 바꾸는 함수인 bin()이 있는 것을 알았다!

def solution(s):
    answer = []
    trial = 0
    zeros = 0
    while (True):
        if s == '1':
            break
        trial += 1
        zeros += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]

    answer = [trial, zeros]
    return answer
