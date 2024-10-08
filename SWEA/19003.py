# 19003. 팰린드롬 문제

# 어떠한 문자열 S가 뒤집어도 S와 동일하다면 팰린드롬이라고 한다.
# 양의 정수 N개의 길이가 같은 문자열이 주어졌을 때,
# 몇 개의 문자열을 고른 후 적당히 재배열해 합쳤을 때 펠린드롬이 되게 해야 함
# 최종 팰린드롬의 길이를 최대화 하라

tc = int(input())

for i in range(1, tc+1):
    n, m = map(int, input().split())
    s = []
    for j in range(n):
        s.append(input())
    # 일단 팰린드롬을 만들되, 문자열을 자유롭게 배치해서 최대의 팰린드롬이 되도록!
    # 일단 여러 종류의 문자열이 존재한다
    # 1. 혼자서 펠린드롬인 경우 -> 최종 문자열의 가운데에 배치할 수 있음
    # 단, 펠린드롬인 문자열은 1개거나 짝이 있어야 한다!
    # 2. 펠린드롬이 아니지만 짝이 있는 경우 -> 짝과 대칭되는 위치에 배치할 수 있음
    # 3. 펠린드롬도 아니고 짝도 없는 경우 -> 갖다 버려야 됨
    cnt = 0
    pelin = 0
    if m % 2 == 0:
        front = m // 2
        back = m // 2
    else:
        front = m // 2 + 1
        back = m // 2
    for j in range(n):
        if s[j] == '0':
            continue
        print(s[j][:front], s[j][back:])
        if s[j][:front] == s[j][back:][::-1]:
            # 펠린드롬을 처음 발견했을 경우
            if pelin == 0:
                for k in range(j+1, n):
                    if s[j] == s[k]:
                        cnt += 1
                        s[k] = '0'
                pelin = 1
                cnt += 1
                s[j] = '0'
            else:
                # 그게 아니면 무조건 짝이 있어야 함
                for k in range(j+1, n):
                    if s[j] == s[k]:
                        cnt += 2
                        s[j] = '0'
                        s[k] = '0'
        else:
            # 펠린드롬이 아닌 경우 나머지 문자열을 돌면서 짝을 찾아야 함
            for k in range(j+1, n):
                if s[j] == s[k][::-1]:
                    cnt += 2
                    s[j] = '0'
                    s[k] = '0'
                    break
    print(f"#{i} {cnt*m}")

            
        