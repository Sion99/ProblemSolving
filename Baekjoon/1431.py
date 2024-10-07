# 시리얼 번호

# 시리얼 번호 알파벳 대문자(A-Z), 숫자(0-9)로 이루어짐

import sys

input = sys.stdin.readline

n = int(input().rstrip())

serials = []

for i in range(n):
    sn = input().rstrip()
    total = 0
    for j in range(len(sn)):
        if '0' <= sn[j] <= '9':
            total += int(sn[j])
    serials.append([len(sn), total, sn])

serials.sort(key=lambda x:(x[0], x[1], x[2]))

for serial in serials:
    print(serial[2])