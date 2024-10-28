# 골드 5 16987. 계란으로 계란치기

# 계란으로 계란을 치게 될 경우 어떤 일이 벌어지나?
# 각 계란에는 내구도와 무게가 정해져 있다.
# 계란으로 계란을 칠 때 각 계란의 내구도는 상대 계란의 무게만큼 깎인다.
# 내구도가 0 이하가 되는 순간 계란은 깨진다.
# 왼쪽부터 차례로 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

# 1. 가장 왼쪽의 계란을 든다
# 2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다.
# 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
# 이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
# 3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다.
# 단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.

# 일렬로 놓인 계란들의 내구도와 무게가 차례대로 주어졌을 때 최대 몇 개의 계란을 깰 수 있나?

def count_broken(arr):
    cnt = 0
    for a in arr:
        if a[0] <= 0:
            cnt += 1
    return cnt

def backtrack(arr, idx):
    global answer
    if idx == len(arr):
        answer = max(answer, count_broken(arr))
        return
    else:
        if arr[idx][0] <= 0:
            backtrack(arr, idx+1)
            return
        
        flag = False
        for i in range(len(arr)):
            if i == idx or arr[i][0] <= 0:
                continue
            arr[idx][0] -= arr[i][1]
            arr[i][0] -= arr[idx][1]
            backtrack(arr, idx+1)
            arr[idx][0] += arr[i][1]
            arr[i][0] += arr[idx][1]
            flag = True
        
        if not flag:
            backtrack(arr, idx+1)


n = int(input())
eggs = []
for i in range(n):
    w, h = map(int, input().split())
    eggs.append([w, h])


answer = 0
backtrack(eggs, 0)

print(answer)