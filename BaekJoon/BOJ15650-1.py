n, m = map(int, input().split())

v = [0] * n
arr = [] 

def sol(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return 
    
    for i in range(idx, n):
        if not v[i]:
            v[i] = 1
            arr.append(i + 1)
            sol(depth + 1, i + 1, n, m)
            v[i] = 0 
            arr.pop()

sol(0, 0, n, m)
            