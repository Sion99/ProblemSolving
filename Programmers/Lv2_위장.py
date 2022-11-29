# 11/29 21:00-
# 생각보다 많이 어려운데? 22:23 까지 못품..

# 결국 거의 두 시간 쓰고 다른 사람 아이디어를 통해 풀었다
# 코드를 본 것은 아니지만 수학적 접근법을 제시해줘서 덕분에 풀 수 있었다.
# 내가 하려 했던 것은 combinations을 이용해 조합을 구하여 어떻게 어떻게 하려고 했는데,
# 굉장히 비효율적이고 오류 많은 코드였던 거 같다

def solution(clothes):
    answer = 0
    clth = []
    for i in clothes:
        clth.append(i[1])

    clth.sort()
    number = []
    temp = list(set(clth))
    for i in temp:
        number.append(clth.count(i))

    func = 1
    for i in range(len(number)):
        func = func * (1+number[i])

    func = func - 1

    print(func)
    answer = func
    return answer
