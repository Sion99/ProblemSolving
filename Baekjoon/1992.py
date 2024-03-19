# 쿼드트리

# 흰점 0, 검은점 1
# 위 아래 4개 점을 묶어 동일한 색으로 압축

# 주어진 영상이 모두 0 -> 압축 결과는 0
# 주어진 영상이 모두 1 -> 압축 결과는 1
# 왼쪽 위, 오른쪽 위
# 왼쪽 아래, 오른쪽 아래
# 4개 영역을 압축한 결과를 차례대로 괄호 안에 묵어서 사용

def check(x1, y1, size):
    first = matrix[x1 - 1][y1 - 1]
    for i in range(x1, x1 + size):
        for j in range(y1, y1 + size):
            if matrix[i - 1][j - 1] != first:
                return False
    return True

def color(x1, y1):
    return matrix[x1 - 1][y1 - 1]

def divide(x1, y1, size):
    if size == 1:
        print(color(x1, y1), end="")
    else:
        if check(x1, y1, size):
            print(color(x1, y1), end="")
        else:
            print("(", end="")
            divide(x1, y1, size // 2)
            divide(x1, y1 + size // 2, size // 2)
            divide(x1 + size // 2, y1, size // 2)
            divide(x1 + size // 2, y1 + size // 2, size // 2)
            print(")", end="")

matrix = list()
N = int(input())

for _ in range(N):
    matrix.append(list(input()))

divide(1, 1, N)