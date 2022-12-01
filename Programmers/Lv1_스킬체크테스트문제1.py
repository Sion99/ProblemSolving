import math

n = 1000  # 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
# 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

print(array.count(True))
