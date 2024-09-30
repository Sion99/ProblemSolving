# 포도주 시식

# 포도주 시식 두 가지 규칙
# 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마시고, 원래 위치 다시 놓기
# 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다

# 될 수 있는 대로 많은 양의 포도주를 맛보기 위해 포도주 잔 선택
# 1~n 까지 포도주 잔, 각 포도주 잔에 들어있는 양 주어짐

n = int(input())
wines = []

for i in range(n):
    wines.append(int(input()))

arr = []

for i in range(n):
    cnt = 0
    for j in range(i, n):
        if cnt == 2:
            cnt = 0
            continue
        

print(wines)