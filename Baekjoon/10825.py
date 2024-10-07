# 국영수

# 정렬문제
import sys

input = sys.stdin.readline

n = int(input().rstrip())

arr = []
for i in range(n):
    score = list(input().rstrip().split())
    arr.append([score[0], int(score[1]), int(score[2]), int(score[3])])

arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for student in arr:
    print(student[0])