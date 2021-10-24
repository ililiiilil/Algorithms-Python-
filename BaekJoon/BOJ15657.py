n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def sol(d, idx, n, m):
    if d == m:
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(idx, n):
        ans.append(arr[i])
        sol(d + 1, i, n, m)
        ans.pop()

sol(0, 0, n, m)