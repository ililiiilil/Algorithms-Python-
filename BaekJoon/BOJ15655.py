n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

v = [0] * n

def sol(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(idx, n):
        if not v[i]:
            v[i] = 1
            ans.append(arr[i])
            sol(depth + 1, i + 1, n, m)
            v[i] = 0 
            ans.pop()

sol(0, 0, n, m)