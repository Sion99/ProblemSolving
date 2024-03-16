import sys

# 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값
# 진실을 아는 사람이 있는 파티에서는 진실만 이야기
# 진실을 아는 사람이 없는 파티에서는 과장된 이야기

# 사람 수 N, 파티 수 M
# 진실을 아는 사람 수, 번호
# 각 파티마다 오는 사람의 수, 번호
people = []

def find(n):
    if people[n] == n:
        return people[n]
    people[n] = find(people[n])
    return people[n]

def merge(x, y):
    x = find(x)
    y = find(y)
    if x in knowing and y in knowing:
        return
    if x in knowing:
        people[y] = x
    elif y in knowing:
        people[x] = y
    else:
        if x < y:
            people[y] = x
        else:
            people[x] = y


n, m = map(int, sys.stdin.readline().split())
people = list(range(n + 1))
knowing = list(map(int, sys.stdin.readline().split()))[1:]


# 모든 파티를 순차적으로 돌면서 만약에 knowing이 있다 -> 해당 파티 내 not_knowing도 knowing으로 이동
# 반복을 계속 할 것인가? -> 아니면 그래프로 접근할 것인가?
# knowing 각 원소들을 그래프의 시작점으로 두고, 파티를 추가해보기
# 결국은 Union find

parties = []
ans = 0

for _ in range(m):
    party = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(party) - 1):
        merge(party[i], party[i+1])
    parties.append(party)

for party in parties:
    for i in range(len(party)):
        if find(party[i]) in knowing:
            break
    else:
        ans += 1

print(ans)
