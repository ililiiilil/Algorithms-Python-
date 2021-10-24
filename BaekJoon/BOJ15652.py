n, m = map(int, input().split())

arr = []

def sol(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(idx, n):
        arr.append(i + 1)
        sol(depth + 1, i, n, m)
        arr.pop()
        
sol(0, 0, n, m)