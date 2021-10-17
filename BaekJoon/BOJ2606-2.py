n = int(input())
m = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    global cnt
    visited[v] = 1

    for i in range(1, n + 1):
        if visited[i] == 0 and matrix[v][i] == 1:
            visited[i] = 1
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

