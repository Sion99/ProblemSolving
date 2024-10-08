# 17319. 문자열문자열

# 알파벳 소문자로 이루어진 문자열 하나를 받아 그대로 두 번 연달아 썼다.
# 문자열이 주어질 때, 이 문자열이 두 번 연달아 써서 만들어 낼 수 있는 문자열인지 판단

tc = int(input())

for i in range(1, tc+1):
    n = int(input())
    s = input()

    if n % 2 != 0:
        print(f"#{i} No")
    else:
        if s[:n//2] == s[n//2:]:
            print(f"#{i} Yes")
        else:
            print(f"#{i} No")