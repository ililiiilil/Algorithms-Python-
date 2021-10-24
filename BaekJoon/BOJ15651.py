n, m = map(int, input().split())

v = [0] * n 
arr = []

def sol(d, n, m):
    if d == m:
        print(' '.join(map(str, arr)))
        return 
    
    for i in range(n):
        if not v[i]:
            arr.append(i + 1)
            sol(d + 1, n, m)
            arr.pop()

sol(0, n, m)