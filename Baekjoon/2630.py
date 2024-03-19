# 색종이 만들기
# 정사각형 모양 종이
# 흰색 or 파란색
# 정사각형 모양의 흰색 or 파란색 색종이

# 자르는 규칙
# 전체가 하나의 색이 아닐시
# 가로 세로 중간을 잘라 4개로 만듦
# 잘라진 각각의 종이에 대해서 다시 반복

# 각 부분이 하나의 색으로 될 때까지 또는 한 칸만 남아 더 이상 자를 수 없을 때 까지 반복

# 최종적으로 만들어진 흰색 색종이 & 파란색 색종이 개수 구하기

def check(x1, y1, size):
    first = matrix[x1 - 1][y1 - 1]
    for i in range(size):
        for j in range(size):
            if matrix[x1 - 1 + i][y1 - 1 + j] != first:
                return False
    return True
    
def count(x1, y1):
    global white, blue
    if matrix[x1 - 1][y1 - 1] == 0:
        white += 1
    else:
        blue += 1


def divide(x1, y1, size):
    if size == 1:
        count(x1, y1)
    else:
        if check(x1, y1, size):
            count(x1, y1)
        else:
            divide(x1, y1, size // 2)
            divide(x1 + size // 2, y1, size // 2)
            divide(x1, y1 + size // 2, size // 2)
            divide(x1 + size // 2, y1 + size // 2, size // 2)



white = 0
blue = 0

N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))


divide(1, 1, N)

print(white)
print(blue)