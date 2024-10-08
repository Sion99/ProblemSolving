# 2071. 평균값 구하기

# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램 작성
# 소수점 첫째 자리에서 반올림한 정수 출력

t = int(input())

for i in range(1, t+1):
    arr = list(map(int, input().split()))
    avg = round(sum(arr) / 10)
    print(f"#{i} {avg}")