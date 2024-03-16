from collections import deque

# BFS로 그래프 탐색하기
# 각 노드를 채워넣고, 처음부터 돌면서 그래프 그리기

def bfs(n):
    global check
    visited[n] = True
    for i in matrix[n]:
        if not visited[i]:
            bfs(i)
            check += 1

testcase = 0

while True:
    N = int(input())
    if N == 0:
        break
    testcase += 1
    graph = set()
    manito = []
    for _ in range(N):
        a, b = input().split()
        manito.append([a, b])
        graph.add(a)
        graph.add(b)
    
    graph = list(graph)
    matrix = [[] for _ in range(N + 1)]
    people = dict()
    for i in range(N):
        people[graph[i]] = i + 1
    
    for a, b in manito:
        k = people.get(a)
        t = people.get(b)
        matrix[k].append(t)

    result = []
    answer = 0
    for i in range(1, N + 1):
        if i in result:
            continue
        check = 1
        visited = [False] * (N + 1)
        bfs(i)
        if check == visited.count(True):
            for i in range(len(visited)):
                if visited[i] == True:
                    if i not in result:
                        result.append(i)
            answer += 1
    
    print(testcase, answer)

# 연결 고리 체크

        
