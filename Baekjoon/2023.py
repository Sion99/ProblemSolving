# 골드 5 2023. 신기한 소수

# 7331인은 소수인데 733도 소수이고, 73도 소수이고, 7도 소수이다
# 왼쪽부터 1자리, 2자리, 3자리, 4자리 모두 소수이다
# 이런 숫자를 신기한 소수라고 한다
# 자리수 N이 주어졌을 때, N자리 신기한 소수를 모두 찾아라

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n**1//2 + 1):
        if n % i == 0:
            return False
    return True

def find_strange_prime(n):
    global primes
    # n자리 신기한 소수를 찾는다
    if n == 1:
        # 첫째자리라면
        primes.append([2, 3, 5, 7])
    else:
        # 첫째자리부터 하나하나 들였고, 이제 n자리 차례
        find_strange_prime(n-1)
        temp = []
        for i in range(len(primes[n-2])):
            for j in range(10):
                if is_prime(primes[n-2][i] * 10 + j):
                    temp.append(primes[n-2][i] * 10 + j)
        primes.append(temp)
                    
                    
n = int(input())

primes = []

# 왼쪽부터 1자리, 2자리, 3자리 .. 모두 소수여야 하기에
# 가장 첫 자리는 무조건 소수임 -> 2, 3, 5, 7
# 두 번째 자리까지도 무조건 두자리수 소수여야 함
# 이거는 n자리수 소수 구하는 걸 만들고 이걸 재귀로 쓰든지 해야 할듯?
# 1자리수 소수 -> 2자리수 소수 -> 3자리수 소수..

find_strange_prime(n)

for prime in primes[n-1]:
    print(prime)