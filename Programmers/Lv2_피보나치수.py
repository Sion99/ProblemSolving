def solution(n):
    answer = 0
    fib = [0, 1]
    for i in range(2, n+1):
        fibonacci = fib[i-1] + fib[i-2]
        fib.append(fibonacci)

    answer = fib[-1] % 1234567
    return answer
