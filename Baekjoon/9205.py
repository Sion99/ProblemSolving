# 골드 5 9205. 맥주 마시면서 걸어가기

# 맥주를 마시면서 걸어가기
# 맥주 한 박스 (20병) 들고 출발
# 50미터에 한 병씩 마신다

# 중간에 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다.
# 대신, 박스에 들어있는 맥주는 20병 넘을 수 없음
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 함

# 편의점, 출발, 도착 지점 좌표를 알 때, 맥주가 부족하지 않게 도착할 수 있는가?

# 송도는 직사각형으로 생긴 도시
# 두 좌표 사이의 거리는 x 좌표 차 + y 좌표 차 (맨해튼 거리)

# 일단 세 점으로 도시 범위를 좁힐 필요가 있음
# 가장 큰 x값을 x 바운더리, 가장 큰 y값을 y 바운더리로 생각해야할듯?
# 값이 음수일 수도 있음 -> 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    # 편의점 수
    n = int(input())
    arr = []
    for i in range(n+2):
        arr.append(tuple(map(int, input().split())))
    
    # 맵 새로 만들기
    max_x = 32767
    min_x = -32768
    max_y = 32767
    min_y = -32768
    for a in arr:
        max_x = max(max_x, a[0])
        min_x = min(min_x, a[0])
        max_y = max(max_y, a[1])
        min_y = min(min_y, a[1])
    
    width = abs(max_y - min_y)
    height = abs(max_x - min_x)

    visited = [[False for _ in range(width)] for _ in range(height)]
    for i in range(len(arr)):
        arr[i][0] += height


    


    