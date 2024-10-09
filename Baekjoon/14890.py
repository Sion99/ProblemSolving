# 골드 3 14890. 경사로

# 크기 N*N 지도, 각 칸에는 높이 기록
# 지도에서 지나갈 수 있는 길이 몇 개인지?
# 길이란 한 행 또는 한 열 전부 -> 수직 수평의 직선 하나

# N * N 의 지도에는 길은 총 2N개가 존재한다.
# 지나갈 수 있는 길이란, 길에 속한 모든 칸의 높이가 모두 같아야 한다.
# 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
# 경사로는 높이가 항상 1이며, 길이는 L이다.
# 경사로는 무제한으로 설치할 수 있고, 낮은 칸과 높은 칸을 연결하며, 다음 조건을 만족해야 함.

# 1. 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 함
# 2. 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다
# 3. 경사로를 놓은 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.

# 아래와 같은 경우에는 경사로를 놓을 수 없다.

# 1. 경사로를 놓은 곳에 또 경사로를 놓은 경우
# 2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 4. 경사로를 놓다가 범위를 벗어나는 경우

# 경사로 배치 가능한 구간 예시
# 2
# 2 1 1 1

# 경사로 배치 불가능한 구간 예시
# 3
# 3
# 3 1 1 1

# 2     2
# 2 1 1 2

# 딱 봐도 길이 정렬이 되어 있나 그건 거 같은데?
# 대신에 길이 차가 1이 나게끔 완만히 정렬되어야 함
# 3 2 2 1 1 1 -> 가능
# 3 3 3 3 3 3 -> 가능
# 2 3 3 3 3 3 -> 불가능 (경사로 길이 너무 짧음)
# 1 1 1 2 2 2 -> 가능
# 1 1 1 3 3 1 -> 불가능
# 1 1 2 3 3 2 -> 불가능

# 지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램 작성하라

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 경사로를 놓을 수 있는지 확인하는 함수
def can_place_slope(line):
    used = [False] * n  # 경사로를 놓은 위치를 기록할 리스트
    for i in range(n - 1):
        if line[i] == line[i + 1]:  # 높이가 같은 경우
            continue
        elif line[i] + 1 == line[i + 1]:  # 올라가는 경사로
            for j in range(i, i - l, -1):  # 경사로를 놓을 수 있는지 확인
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        elif line[i] - 1 == line[i + 1]:  # 내려가는 경사로
            for j in range(i + 1, i + 1 + l):  # 경사로를 놓을 수 있는지 확인
                if j >= n or line[j] != line[i + 1] or used[j]:
                    return False
                used[j] = True
        else:  # 높이 차이가 1이 아니면 경사로를 놓을 수 없음
            return False
    return True

ans = 0

# 가로 방향 확인
for i in range(n):
    if can_place_slope(board[i]):
        ans += 1

# 세로 방향 확인
for j in range(n):
    column = [board[i][j] for i in range(n)]
    if can_place_slope(column):
        ans += 1

print(ans)
