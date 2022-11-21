# S4 듣보잡
import sys

n, m = map(int, input().split())


haventheard = [sys.stdin.readline().strip() for i in range(n)]
haventseen = [sys.stdin.readline().strip() for j in range(m)]
heardseen = list(sorted(set(haventheard) & set(haventseen)))

print(len(heardseen))
for i in range(len(heardseen)):
    print(heardseen[i], end='\n')
