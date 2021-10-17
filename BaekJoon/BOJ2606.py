n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]
visited = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

def dfs(v):
    visited[v] = 1

    for i in range(n):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(0)
print(sum(visited) - 1)