import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
matrix = [[0] *(n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

def dfs(v):
    visited[v] = 1

    for k in range(1, n + 1):
        if visited[k] == 0 and matrix[v][k] == 1:
            dfs(k)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1 

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)