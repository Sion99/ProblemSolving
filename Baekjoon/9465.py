# 스티커

# 스티커 2n개 구매
# 2행 n열, 2xn 배치

# 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 사용 불가
# 뗀 스티커의 좌우 위아래 스티커는 사용 불가

# 떼어낸 각 스티커의 점수의 합이 최대가 되게
# 2n개 스티커 중에 점수의 합이 최대가 되면서 서로 변을 공유하지 않는 스티커 집합
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))

    # print(arr)

    # dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]
    
    # # 0은 선택한 것, 1은 선택 안한 것
    # dp[0][0][0] = arr[0][0]
    # dp[0][0][1] = 0

    # dp[1][0][0] = arr[1][0]
    # dp[1][0][1] = 0

    # print(dp)

    # for i in range(1, n):
    #     # j가 0인 경우 (위쪽)
    #     # [0][i]를 선택한 경우
    #     dp[0][i][0] = max(dp[1][i-1][0], dp[1][i-1][1]) + arr[0][i]
    #     # [0][i]를 선택하지 않은 경우
    #     dp[0][i][1] = max(dp[0][i-1][0], dp[0][i-1][1], dp[1][i-1][0], dp[1][i-1][1])

    #     # j가 1인 경우 (아래쪽)
    #     # [1][i]를 선택한 경우
    #     dp[1][i][0] = max(dp[0][i-1][0], dp[0][i-1][1]) + arr[1][i]
    #     # [1][i]를 선택하지 않은 경우
    #     dp[1][i][1] = max(dp[0][i-1][0], dp[0][i-1][1], dp[1][i-1][0], dp[1][i-1][1], dp[0][i][0], dp[0][i][1])

    # print(max(dp[0][n-1][0], dp[0][n-1][1], dp[1][n-1][0], dp[1][n-1][1]))


    dp = [[0] * n for _ in range(3)]
    
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[2][0] = 0

    for i in range(1, n):
        # 위쪽 스티커 선택
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + arr[0][i]
        # 아래쪽 스티커 선택
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + arr[1][i]
        # 둘다 선택 안함
        dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
    
    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))

# 조금씩 조금씩 DP에 익숙해져가는 중..