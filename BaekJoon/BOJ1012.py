from collections import deque

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        if graph[n][i] == 1:

            q = deque()
            x, y = n, i
            q.append((x, y))
            
            while q:
                for j in range(4):
                    nx = dx[j] + x
                    ny = dx[i] + y 

                    if nx > m or ny > n or nx < -1 or ny < -1:
                        continue
                    
                    if graph[nx][ny] == 0:
                        continue

                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0 
                        cnt += 1
                        q.append((nx, ny))

    print(cnt)

#추후에 다시한번..
    
