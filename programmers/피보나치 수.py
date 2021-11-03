def fibo(n):
    if n < 2:
        return 1 
    return fibo(n - 1) + fibo(n - 2)

def solution(n):

    return fibo(n - 1) % 1234567

print(solution(6))