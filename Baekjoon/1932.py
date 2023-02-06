def solution(triangle):
    answer = 0
    dp = [[0]*len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][i-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    answer = max(max(dp))
    return answer


n = int(input())
triangle = []
for i in range(0, n):
    triangle.append(list(map(int, input().split())))

print(solution(triangle))
