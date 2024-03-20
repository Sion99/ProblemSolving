# 1로 만들기

# X에 대한 연산 3가지
# X가 3의 배수 -> 3으로 나눔
# X가 2의 배수 -> 2로 나눔
# X - 1

# N이 주어졌을 때, 연산을 사용해 1 만들기 -> 연산의 최솟값

from collections import deque

N = int(input())

dq = deque()
dq.append((N, 0))

visited = [''] * 1000001

while dq:
    cur, cnt = dq.popleft()
    if cur == 1:
        print(cnt)
        print(N, end="")
        print(visited[cur])
        break
    if cur % 3 == 0:
        nx = cur // 3
        if nx >= 1:
            if not visited[nx]:
                visited[nx] = visited[cur] + ' ' + str(nx)
                dq.append((nx, cnt + 1))
    if cur % 2 == 0:
        nx = cur // 2
        if nx >= 1:
            if not visited[nx]:
                visited[nx] = visited[cur] + ' ' + str(nx)
                dq.append((nx, cnt + 1))
    nx = cur - 1
    if nx >= 1:
        if not visited[nx]:
            visited[nx] = visited[cur] + ' ' + str(nx)
            dq.append((nx, cnt + 1))

