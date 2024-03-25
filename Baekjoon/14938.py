# 서강그라운드

# 각 지역은 일정한 길이로 다른 지역과 연결되어 있음 (양방향)
# 낙하한 지역을 중심으로 수색 범위 m 이내의 모든 지역의 아이템 습득 가능
# 낙하 지역에서 얻을 수 있는 아이템 최대 개수

import sys
import heapq

input = sys.stdin.readline

INF = 1e8

def dijkstra(node):
    que = []
    distance[node] = 0
    heapq.heappush(que, (0, node))

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))




N, M, R = map(int, input().split())

item = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))

ans = 0
for node in range(N):
    distance = [INF] * N
    dijkstra(node)
    cnt = 0
    for i in range(N):
        if distance[i] <= M:
            cnt += item[i]

    ans = max(ans, cnt)
print(ans)
