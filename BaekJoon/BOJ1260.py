from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1 

visited = [0] * (n + 1)

def dfs(start):
    visited[start] = 1
    print(start, end = ' ')

    for i in range(1, n + 1):
        if visited[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)

    visited[start] = 1

    while q:
        node = q.popleft()
        print(node, end = ' ')
        for i in range(1, n + 1):
            if visited[i] == 0 and graph[node][i] == 1:
                q.append(i)
                visited[i] = 1

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)