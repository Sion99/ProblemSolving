n = input()
m = int(input())
order = input().split()
print(order)

available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in order:
    available.remove(int(i))
print(available)

# 첫번째로, 남은 숫자를 조합해서 가장 가까운 숫자를 만들어낸다
# 원하는 채널에 한칸씩 다가가면서 카운트

# 어떻게 가장 가까운 숫자를 만들 것인가?
# 끝에서부터 맞출까?
# 보통은 앞에서부터 맞추는 것이 좋을 것
# 하지만

# for i in n:
#     for j in available:
#         if i == j:
