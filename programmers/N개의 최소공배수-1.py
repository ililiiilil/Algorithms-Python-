def gcd(a, b):
    if not a % b:
        return b 
    
    else:
        return gcd(b, a % b)

def solution(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i - 1] * arr[i] // gcd(arr[i], arr[i - 1])
    
    return arr[-1]