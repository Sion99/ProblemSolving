# 퇴사

# N+1일째 되는 날 퇴사하기 위해, 남은 N일 동안 최대한 많은 상담
# 하루에 하나씩 서로 다른 사람의 상담
# 상담을 완료하는데 걸리는 기간 Ti, 상담 금액 Pi

# 상담을 적절히 했을 때, 최대 수익

n = int(input())
t = []
p = []

for i in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

print(t)
print(p)

pay = [[0] * 2 for _ in range(n)]

print(pay)

for i in range(n):
    