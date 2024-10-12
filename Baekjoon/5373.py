# 플레티넘 5 5373. 큐빙

# 큐브는 3차원 퍼즐이다.
# 3*3*3 개의 정육면체로 이루어져 있으며
# 퍼즐을 풀려면 각 면에 있는 아홉 개의 칸이 동일해야 한다.

# 큐브는 각 면을 양방향으로 90도 만큼 돌릴 수 있도록 만들어져 있다.
# 회전이 마친 이후에는 다른 면을 돌릴 수 있다.

# 이 문제에서는 큐브가 모두 풀린 상태에서 시작
# 윗 면은 흰색, 아랫면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색

#    흰 (위)
# 초  오   파
#    노 (바닥)
#    빨

# 큐브를  순서 대로 돌리고, 모두 돌린 다음에 가장 윗 면의 색상을 구하라
# 즉, 윗 면의 3 * 3 칸 색깔 출력
# 일단 정육면체의 각 면을 구현을 먼저 해
# 그리고 나서, 회전 하려고 할 때마다 회전 대상의 면들을 일렬로 집합시키고, 회전한다음 다시 적용해
# 이거 무한 반복
# 어차피 회전할 때 영향 받는 거는 한 줄만이다!


def rotate_face(face):
    return [list(row) for row in zip(*face[::-1])]

def rotate_cube(cube, face, direction):
    if face == 'U':
        if direction == '+':
            cube[0] = rotate_face(cube[0])
            cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[4][0], cube[1][0], cube[2][0], cube[3][0]
        else:
            cube[0] = rotate_face(rotate_face(rotate_face(cube[0])))
            cube[1][0], cube[2][0], cube[3][0], cube[4][0] = cube[2][0], cube[3][0], cube[4][0], cube[1][0]
    elif face == 'D':
        if direction == '+':
            cube[5] = rotate_face(cube[5])
            cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[2][2], cube[3][2], cube[4][2], cube[1][2]
        else:
            cube[5] = rotate_face(rotate_face(rotate_face(cube[5])))
            cube[1][2], cube[2][2], cube[3][2], cube[4][2] = cube[4][2], cube[1][2], cube[2][2], cube[3][2]
    elif face == 'F':
        if direction == '+':
            cube[1] = rotate_face(cube[1])
            cube[0][2], [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[5][0], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]], cube[0][2][::-1], [cube[4][0][0], cube[4][1][0], cube[4][2][0]][::-1], cube[5][0]
        else:
            cube[1] = rotate_face(rotate_face(rotate_face(cube[1])))
            cube[0][2], [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[5][0], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[4][0][0], cube[4][1][0], cube[4][2][0]], cube[5][0][::-1], [cube[2][0][2], cube[2][1][2], cube[2][2][2]][::-1], cube[0][2]
    elif face == 'B':
        if direction == '+':
            cube[3] = rotate_face(cube[3])
            cube[0][0], [cube[2][0][0], cube[2][1][0], cube[2][2][0]], cube[5][2], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]], cube[0][0][::-1], [cube[2][0][0], cube[2][1][0], cube[2][2][0]][::-1], cube[5][2]
        else:
            cube[3] = rotate_face(rotate_face(rotate_face(cube[3])))
            cube[0][0], [cube[2][0][0], cube[2][1][0], cube[2][2][0]], cube[5][2], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] = [cube[2][0][0], cube[2][1][0], cube[2][2][0]], cube[5][2][::-1], [cube[4][0][2], cube[4][1][2], cube[4][2][2]][::-1], cube[0][0]
    elif face == 'L':
        if direction == '+':
            cube[2] = rotate_face(cube[2])
            [cube[0][0][0], cube[0][1][0], cube[0][2][0]], [cube[1][0][0], cube[1][1][0], cube[1][2][0]], [cube[5][0][0], cube[5][1][0], cube[5][2][0]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]], [cube[0][0][0], cube[0][1][0], cube[0][2][0]], [cube[1][0][0], cube[1][1][0], cube[1][2][0]], [cube[5][2][0], cube[5][1][0], cube[5][0][0]]
        else:
            cube[2] = rotate_face(rotate_face(rotate_face(cube[2])))
            [cube[0][0][0], cube[0][1][0], cube[0][2][0]], [cube[1][0][0], cube[1][1][0], cube[1][2][0]], [cube[5][0][0], cube[5][1][0], cube[5][2][0]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[1][0][0], cube[1][1][0], cube[1][2][0]], [cube[5][0][0], cube[5][1][0], cube[5][2][0]], [cube[3][2][2], cube[3][1][2], cube[3][0][2]], [cube[0][2][0], cube[0][1][0], cube[0][0][0]]
    elif face == 'R':
        if direction == '+':
            cube[4] = rotate_face(cube[4])
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][1][0], cube[3][2][0]] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[0][2][2], cube[0][1][2], cube[0][0][2]]
        else:
            cube[4] = rotate_face(rotate_face(rotate_face(cube[4])))
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][1][0], cube[3][2][0]] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[5][2][2], cube[5][1][2], cube[5][0][2]]

def solve_cube():
    t = int(input())
    for _ in range(t):
        cube = [[['w']*3 for _ in range(3)],
                [['r']*3 for _ in range(3)],
                [['g']*3 for _ in range(3)],
                [['o']*3 for _ in range(3)],
                [['b']*3 for _ in range(3)],
                [['y']*3 for _ in range(3)]]
        n = int(input())
        rotations = input().split()
        for rotation in rotations:
            rotate_cube(cube, rotation[0], rotation[1])
        for row in cube[0]:
            print(''.join(row))

solve_cube()