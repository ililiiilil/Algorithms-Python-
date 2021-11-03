def fibo(n):
    if n < 2:
        return 1 
    return fibo(n - 1) + fibo(n - 2)

def solution(n):

    return fibo(n - 1) % 1234567

#재귀함수로는 깊이문제와함께 시간이 너무걸리는듯.
#새로운 방법 찾아보기

