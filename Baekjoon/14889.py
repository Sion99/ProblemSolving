# 스타트와 링크

# 딱 짝수로 이루어진 N명
# N/2 명으로 이루어진 1, 2팀으로 나누어야 함

# 1 ~ N번까지 배정, 능력치 조사
# 능력치 S(i, j) = i번 사람과 j번 사람이 같은 팀일때 팀에 더해지는 능력치
# 팀 능력치는 팀의 모든 S(i, j) 합
# i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S(i, j), S(j, i)이다

# 1 2팀의 능력치 차이를 최소로 하려고 한다.

import sys

def backtrack(arr, selected, start, n, m):
    global teams
    if len(selected) == m:
        temp = []
        for s in selected:
            temp.append(players[s])
        teams.append(temp)
    else:
        for i in range(start, n):
            selected.append(i)
            backtrack(arr, selected, i+1, n, m)
            selected.pop()

input = sys.stdin.readline

n = int(input().rstrip())

# i, j의 조합 전부 구해야 할 거 같은데?

synergy = []

for _ in range(n):
    synergy.append(list(map(int, input().rstrip().split())))

players = [i for i in range(n)]

teams = []

total_synergy = 0

backtrack(players, [0], 1, n, n//2)

ans = 1000000
for team in teams:
    # 우리팀과 상대팀의 시너지 격차 계산
    # 우리팀 먼저
    start_synergy = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            start_synergy += synergy[team[i]][team[j]]
            start_synergy += synergy[team[j]][team[i]]
    
    # 상대팀
    opponents = []
    for i in range(n):
        if i not in team:
            opponents.append(i)
    link_synergy = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            link_synergy += synergy[opponents[i]][opponents[j]]
            link_synergy += synergy[opponents[j]][opponents[i]]
    
    ans = min(ans, abs(start_synergy - link_synergy))

print(ans)
