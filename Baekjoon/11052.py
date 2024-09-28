# 8가지 카드가 있음
# 카드는 카드팩의 형태로만 구매할 수 있고, 카드팩의 종류는 카드1개~N개 포함된 카드팩 총 N가지

# 돈을 최대한 많이 지불해서 카드 N개 구매

# p1 -> 1,  p2 -> 5, p3 -> 6, p4 -> 7인 경우 카드 4개를 갖기 위한 금액 최댓값 10원 p2 * 5

# 카드팩은 동일한 거 여러개 구매 가능
# DP 문제임

n = int(input())
packs = list(map(int, input().split()))

arr = packs[:]

for i in range(n):
    for j in range(i):
        arr[i] = max(arr[i], arr[i - j - 1] + packs[j])
print(arr[n - 1])