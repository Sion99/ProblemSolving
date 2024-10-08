# 16910. 원 안의 점

# N이 주어질 때, 원점을 중심으로 반지름이 N인 원 안에 포함되는 좌표의 개수
# 반지름이 N인 원 안(가장자리 포함)의 점 개수를 구하라

# x, y가 양수인 것만 계산해서 4배 하면 되는 거 아닌가?
# x 또는 y 절편 중 하나만 구해서 4배해서 더해주면 될 듯

t = int(input())

for i in range(1, t+1):
    n = int(input())

    cnt = 0
    for x in range(n+1):
        for y in range(1, n+1):
            if x**2 + y**2 <= n**2:
                cnt += 1
    
    cnt *= 4
    cnt += 1 # 이거는 (0, 0)의 몫
    print(f"#{i} {cnt}")
