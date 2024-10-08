# 스타트와 링크

# 딱 짝수로 이루어진 N명
# N/2 명으로 이루어진 1, 2팀으로 나누어야 함

# 1 ~ N번까지 배정, 능력치 조사
# 능력치 S(i, j) = i번 사람과 j번 사람이 같은 팀일때 팀에 더해지는 능력치
# 팀 능력치는 팀의 모든 S(i, j) 합
# i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 S(i, j), S(j, i)이다

# 1 2팀의 능력치 차이를 최소로 하려고 한다.

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input().rstrip())

# i, j의 조합 전부 구해야 할 거 같은데?

synergy = []

for _ in range(n):
    synergy.append(list(map(int, input().rstrip().split())))

players = [i for i in range(n)]

comb = list(combinations(players, 2))

for c in comb:
    s1 = synergy[c[0]][c[1]]
    s2 = synergy[c[1]][c[0]]
    synergy[c[0]][c[1]] = s1 + s2
    synergy[c[1]][c[0]] = s1 + s2

print(synergy)

team = list(combinations(players, n//2))

# 모든 팀 경우의 수를 구해서, 각각의 팀 시너지 총합을 다 구한다
# 그 다음, 

print(team)