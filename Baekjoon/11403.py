# 경로 찾기

# 가중치 없는 방향 그래프 G -> 모든 정점 (i, j)에 대하여 i -> j 경로 있는지 찾기

def dfs(i, j):
    # 만약 출발지(i)에서 목적지(j)까지 간선이 존재한다
    if matrix[i][j] == 1:
        return 1
    # 만약 간선이 존재하지 않는다 -> 다음 노드로 이동
    for idx in range(N):
        # 출발지(i)에서 다음 노드(idx)로 가는 길이 있을때
        if matrix[i][idx] == 1 and visited[idx] == False:
            # 해당 노드로 이동, 해당 노드에서 목적지와 길이 있는지 체크 (있으면 1, 없으면 0 반환)
            # 즉, 재귀가 반복되어도 끝에서 0 뱉을 것 
            visited[idx] = True
            if dfs(idx, j):
                return 1
    return 0
    

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# i 번째 줄의 j 번째 숫자가 1 -> 간선 존재, 0 -> 없음

graph = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        visited = [False] * 101
        graph[i][j] = dfs(i, j)
        print(graph[i][j], end=" ")
    print()