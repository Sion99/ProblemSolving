# 레벨 햄버거

# 레벨-0 버거 -> 패티만
# 레벨-L 버거 -> 햄버거번, 레벨(L-1) 버거, 패티, 레벨(L-1) 버거, 햄버거번

# L-1 버거 -> BPPPB
# L-2 버거 -> BBPPPBPBPPPBB

# L-N 버거 -> 햄버거 아래 X장 먹었을 때, 먹은 패티 개수


# def find(N, X):
#     if X < N:
#         # 빵만 먹었음
#         return 0
#     else:
#         if X < burger[N - 1] // 2:
#             # 전체 사이즈 절반보다 작을때
#             return find(N - 1, X - burger[N - 1] // 2) + 1
#         else:
#             # 전체 사이즈 절반보다 클때
#             return patty[N - 2] + 1 + find(N - 1, X - burger[N - 1] // 2)
    

def find(n, x):
    # 전 단계 없을때
    if n == 0:
        return x
    if x == 1:
        return 0
    # 가운데보다 전일 경우 -> 전 단계로 보내기 전에 끝에 빵 하나 빼기 - 1
    if x <= 1 + burger[n - 1]:
        return find(n - 1, x - 1)
    # 딱 가운데인 경우 -> 그 전 패티 다 먹고 + 1
    if x == burger[n - 1] + 2:
        return patty[n - 1] + 1
    # 가운데보다 클 경우 -> 그 전 패티 다 먹고 + 1 + 나머지
    if x <= 2 * burger[n - 1] + 2:
        return patty[n - 1] + 1 + find(n - 1, (x - (burger[n - 1] + 2)))
    return patty[n]



N, X = map(int, input().split())

burger = [1] * (N + 1)
patty = [1] * (N + 1)


for i in range(1, N + 1):
    burger[i] = 2 * burger[i - 1] + 3
    patty[i] = 2 * patty[i - 1] + 1

# 이 방식으로 하니까 터짐
# 규칙을 찾아서 개수만 세자.

# 일단 burger[1]
# BPPPB -> 양 끝: B, 가운데: P 5
# burger[2]
# BBPPPBPBPPPBB -> 양 끝: B, 가운데: P, 절반 나눠서 13
# 1 + 13 + 1 + 13 + 1 -> 29
# B(N) = 2*B(N-1) + 3
# P(N) = 2*P(N-1) + 1

print(find(N, X))