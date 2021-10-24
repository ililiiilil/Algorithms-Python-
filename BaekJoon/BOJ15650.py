n, m = map(int, input().split())

visited = [False] * n
arr = []

def sol(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            sol(depth + 1, i + 1, n, m)
            visited[i] = False
            arr.pop()

sol(0, 0, n, m)