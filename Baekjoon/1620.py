# 12/09

# 이 방식대로 하니까 시간 초과 및 틀렸음
# 찾아보니까 index 메소드의 경우 시간복잡도가 O(n)이라고 한다
import sys


def solution1():
    n, m = map(int, input().split())
    pokemon = []
    for i in range(n):
        c = str(input())
        pokemon.append(c)
    for i in range(m):
        d = str(input())
        if d.isdigit():
            print(pokemon[int(d)-1])
        else:
            print(pokemon.index(d)+1)

# 해시로 풀도록 해보자


def solution2():
    n, m = map(int, input().split())
    pokemon_key = {}
    pokemon_value = {}
    for i in range(n):
        input = sys.stdin.readline().strip()
        pokemon_key[i] = input
        pokemon_value[input] = i

    for i in range(m):
        query = sys.stdin.readline().strip()
        if query.isdigit():
            print(pokemon_key[int(query)]-1)
        else:
            print(pokemon_value[query]+1)
