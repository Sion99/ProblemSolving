# 골드 5 1038. 감소하는 수

# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
# 321 -> 감소하는 수
# 950 -> 감소하는 수

# 322 -> 감소하는 수 X
# 958 -> 감소하는 수 X

# N번째 감소하는 수?
# 0 -> 0번째 감소하는 수
# 1 -> 1번째 감소하는 수

# 한자리수는 전부 감소하는 수 (0 ~ 10)

n = int(input())

def is_descending(n):
    num = list(str(n))
    for i in range(len(num)-1):
        if num[i] <= num[i+1]:
            return False
    return True

def find_descending_number(n):
    global arr
    if n >= 11:
        return
    # 이게 결국은 0 ~ 987654321 까지임
    # 결국 무한한 수가 아니기 때문에 처음 find_descending_number 한 번에 계산해서
    # 배열에 집어넣고 들어온 값 찾아서 꺼내주면 될 듯
    temp = []
    for i in range(len(arr[n-2])):
        for j in range(10):
            # 뒤에 일에 자리 하나 추가해주는 것
            if is_descending(arr[n-2][i]*10 + j):
                temp.append(arr[n-2][i]*10 + j)
    arr.append(temp[:])
    find_descending_number(n+1)

arr = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
find_descending_number(2)

arr = arr[-1]
if n >= len(arr):
    print(-1)
else:
    print(arr[n])
