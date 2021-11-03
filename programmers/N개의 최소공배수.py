def gcd(a, b):
    if not a % b:
        return b
    
    else:
        return gcd(b, a % b)

def solution(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] * arr[i] // gcd(arr[i -1], arr[i])
    
    return arr[-1]

#최대공약수 / 최소공배수 구하는 건 공식으로 외우는게 나을듯