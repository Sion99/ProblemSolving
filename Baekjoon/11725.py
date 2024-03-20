# 트리의 부모 찾기

# 루트 없는 트리 -> 트리 루트 1
# 각 노드의 부모 구하기

# 시간초과남 ㅜㅜ
from collections import deque

N = int(input())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 루트는 1부터, 즉 1과 연결된 노드부터 찾아보자.

parent = [0] * (N + 1) 
visited = [False] * (N + 1)

dq = deque([1])
visited[1] = True
while dq:
    cur = dq.popleft()
    for child in tree[cur]:
        if not visited[child]:
            visited[child] = True
            parent[child] = cur
            dq.append(child)
                

for i in range(2, N + 1):
    print(parent[i])

# 1에서 시작하는 DFS, BFS로 풀어보기..? -> 나는 이미 했는데!