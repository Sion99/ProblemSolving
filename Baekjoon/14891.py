# 골드 5 14891. 톱니바퀴

# 8개의 톱니를 가지고 있는 톱니바퀴 4개가 일렬로 놓여짐
# 톱니는 N 또는 S극
# 톱니바퀴 1~4까지

# 톱니바퀴 총 K번 회전 -> 1칸이 1회전임
# 회전은 시계 방향과 반시계 방향 존재

# 톱니바퀴 회전하려면 회전시킬 톱니바퀴와 회전시킬 방향 선택
# 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴 회전 가능
# A를 회전할 때 옆에 있는 B와 서로 맞닿은 톱니 극이 다르면, B는 A가 회전한 반대방향으로 회전

# 제시된 예시를 잘 활용해서 문제를 풀어보자.

from collections import deque

wheel = []
for i in range(4):
    w = input()
    temp = []
    for j in range(8):
        temp.append(int(w[j]))
    wheel.append(temp)
    wheel[i] = deque(wheel[i])

k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    n -= 1
    # n번 톱니를 d 방향으로 회전해라
    # 일단 인접한 애들 극을 확인을 해야 함
    # 톱니바퀴(덱)의 12시 방향부터 시계방향 순서데로 주어짐
    # 0, 1, 2, 3, 4, 5, 6, 7 (위 -> 오른쪽 -> 아래 -> 왼쪽)
    # 즉 옆과 맞닿는 부분은 2, 6 두 개임
    
    # 0번 톱니 -> 1번 체크, 1번 회전이면 2번 체크, 2번 회전이면 3번 체크
    # 1번 톱니 -> 0번, 2번 체크, 2번 회전이면 3번 체크
    # 2번 톱니 -> 1번, 3번 체크, 1번 회전이면 0번 체크
    # 3번 톱니 -> 2번 체크, 2번 회전이면 1번 체크, 1번 회전이면 0번 체크

    if n == 0:
        # 0번인 경우는 오른쪽만 맞닿이 있기 때문에 wheel[0][2]번 체크만 하면 됨
        if wheel[0][2] != wheel[1][6]:
            # 극이 다르면
            if wheel[1][2] != wheel[2][6]:
                # 1, 2번이 극이 다르면
                if wheel[2][2] != wheel[3][6]:
                    # 2, 3번이 극이 다르면
                    # 전부 회전
                    wheel[3].rotate(-d)
                wheel[2].rotate(d)
            wheel[1].rotate(-d)
        wheel[0].rotate(d)
    if n == 1:
        # 1인 경우는 0번과 2번을 체크해야 함
        if wheel[1][6] != wheel[0][2]:
            wheel[0].rotate(-d)
        if wheel[1][2] != wheel[2][6]:
            if wheel[2][2] != wheel[3][6]:
                wheel[3].rotate(d)
            wheel[2].rotate(-d)
        wheel[1].rotate(d)
    if n == 2:
        # 2인 경우는 1번과 3번을 체크해야 함
        if wheel[2][6] != wheel[1][2]:
            if wheel[1][6] != wheel[0][2]:
                wheel[0].rotate(d)
            wheel[1].rotate(-d)
        if wheel[2][2] != wheel[3][6]:
            wheel[3].rotate(-d)
        wheel[2].rotate(d)
    if n == 3:
        # 3인 경우는 2, 1, 0 순으로 체크
        if wheel[3][6] != wheel[2][2]:
            if wheel[2][6] != wheel[1][2]:
                if wheel[1][6] != wheel[0][2]:
                    wheel[0].rotate(-d)
                wheel[1].rotate(d)
            wheel[2].rotate(-d)
        wheel[3].rotate(d)

ans = wheel[0][0] + 2*wheel[1][0] + 4*wheel[2][0] + 8*wheel[3][0]
print(ans)