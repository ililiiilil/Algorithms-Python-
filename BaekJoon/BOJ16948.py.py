from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
s = [[0] * n for i in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            
            if s[nx][ny] == 0:
                s[nx][ny] = s[x][y] + 1 
                q.append((nx, ny))

bfs(r1, c1)                
if s[r2][c2] == 0:
    print(-1)
else:
    print(s[r2][c2])

        


    

