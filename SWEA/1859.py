# 1859. 백만 장자 프로젝트

# 다음의 조건 하에서 사재기를 하여 최대한의 이득을 얻자

# 1. 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
# 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
# 3. 판매는 얼마든지 할 수 있다.

# 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익 얻을 수 있음

# 그리디하게 생각해야 할 거 같은데, 일단 감소하는 시점에서는 판매를 하면 안돼
# 증가하는 시점 시작 점에서 구매를 하고, 제일 고점 (증가가 멈춘 포인트)에 다 팔아야 함
# 극소에서 사고 다음 극대에서 팔기

t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    
    idx = 0
    temp = 0
    for j in range(n-1, -1, -1):
        temp = 1



    print(f"#{i} {total}")
