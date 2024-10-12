# 골드 3 20057. 마법사 상어와 토네이도

# 토네이도를 크기가 N * N 인 격자로 나누어진 모래밭에서 연습
# 토네이도를 시전하면 격자의 가운데 칸 부터 토네이도의 이동이 시작된다.
# 토네이도는 한 번에 한 칸 이동한다.
# 토네이도가 한 칸 이동할 때 마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.

# 토네이도가 x에서 y로 이동할 때, y의 모든 모래가 비율이 적혀있는 칸, 그리고 다음 칸으로 이동한다.
# 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다.
# 다음칸 a로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
# 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.

# 토네이도는 (N-1/2, N-1/2)에서 시작해서 (1, 1)까지 이동한 뒤 소멸한다.
# 모래가 격자의 밖으로 이동할 수도 있다.
# 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양은?

import sys

input = sys.stdin.readline

# 배열을 반시계 방향으로 90도 회전한다.
def rotate(spread):
    new_spread = list(reversed(list(zip(*spread))))
    return new_spread

n = int(input().rstrip())

spread = [[0, 0, 0.02, 0, 0],
          [0, 0.1, 0.07, 0.01, 0],
          [0.05, 0, 0, 0, 0],
          [0, 0.1, 0.07, 0.01, 0],
          [0, 0, 0.02, 0, 0]]
spread1 = rotate(spread)
spread2 = rotate(spread1)
spread3 = rotate(spread2)

# 허리케인 이동방향
hurricane = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# 허리케인 이동방향에 따른 알파 위치
alphas = [[2, 1], [3, 2], [2, 3], [1, 2]]


# 흩날리는 비율방향
sand_spread = [spread, spread1, spread2, spread3]



board = []
for i in range(n):
    board.append(list(map(int, input().rstrip().split())))

# 토네이도 보니까 2번 꺾을 때 마다 1칸 더 늘어남
# c-1, r+1, c+2, r-2, c-3, r+3, c+4, r-4, c-5, r+5, c+6, r-6, c-6 끝
# - + + - - + + - - + + - -
len = 1
# 옆으로 움직이면 true, 위아래로 움직이면 false
is_column = True
sign = [-1, 1, 1, -1]
final = False
cnt = 0

# 일단 가운데에서 0, 0 까지 소용돌이 치며 내용 출력하도록 해보자.
# 시작점 설정
x, y = n//2, n//2
# 한 번 가장자리 닿으면, 그 때부터는 (0, 0) 나올때 까지 len = n-1으로 유지됨
print(board[x][y])
while True:
    if x == 0 and y == 0:
        break
    for i in range(len):
        if is_column:
            # 옆으로 움직인다.
            y += sign[cnt%4]
        else:
            x += sign[cnt%4]
        print(board[x][y])
    # 한 번 이동이 다 끝났으면 꺾어야지
    is_column = -is_column
    # (n-1, 0) 닿는 순간 최종 모드 진입 (3번 꺾고 (0, 0) 도착)
    if x == n-1 and y == 0:
        final = True
        len = n-1

    if not final:
        if cnt % 2 == 1:
            # 같은 길이를 두 번 사용했다면?
            # 이제 길이 늘려줄 차례
            len += 1
        cnt += 1
    
    
    
        
