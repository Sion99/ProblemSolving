# 12/15
# 오랜만에 dp 문제 풀이
# 역시 머릿속으로 하는 것보다는 손으로 직접 그려가면서 하는게 이해가 잘된다
# 30분 정도 걸린듯 ㅠㅠ

def solution(triangle):
    answer = max(max(triangle))
    dp = [[0]*len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    print(dp)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            print(j, len(triangle[i])-1)
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][i-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
            print(triangle)
            print(dp)
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
