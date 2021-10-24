n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

def sol(d, n, m):
    if d == m:
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(n):
        ans.append(arr[i])
        sol(d + 1, n, m)
        ans.pop()

sol(0, n, m)