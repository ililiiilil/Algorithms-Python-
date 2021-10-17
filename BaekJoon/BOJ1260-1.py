from collections import deque

n, m, v = map(int, input().split())

matrix = [[0] * (m + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    visited[v] = 1 
    print(v, end = ' ')
    
    for i in range(1, n + 1):
        if visited[i] == 0 and matrix[v][i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)

    visited[start] = 1 

    while q:
        node = q.popleft()
        print(node, end= ' ')

        for i in range(1, n + 1):
            if visited[i] == 0 and matrix[node][i] == 1:
                q.append(i)
                visited[i] = 1 

dfs(1)
visited = [0] * (n + 1)
print()
bfs(1)