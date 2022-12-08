# 12/07
# 역순으로 접근해서 풀었다

def solution(n):
    ans = 0
    battery = 0

    while (n > 0):
        if n % 2 == 0:
            n = n/2
        else:
            n = n - 1
            battery += 1

    ans = battery
    return ans
