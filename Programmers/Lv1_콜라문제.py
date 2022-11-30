def solution(a, b, n):
    answer = 0
    # 빈 병 a개에서 돌려주는 콜라병 b개, 상빈이가 가지고 있는 빈 병 n개
    # f(a) = b
    total = 0
    while (True):
        if n >= a:
            total += (n//a)*b
            n = n % a + (n//a)*b
        else:
            break

    answer = total
    return answer
