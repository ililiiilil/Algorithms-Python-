from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2] 
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(x, y, l, s):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= l or ny >= l or nx < 0 or ny < 0:
                continue 
            
            if s[nx][ny] == 1:
                continue

            if s[nx][ny] == 0:
                s[nx][ny] = s[x][y] + 1 
                q.append((nx, ny))

t = int(input())

for _ in range(t):
    l = int(input())
    s = [[0] * l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        print(0)
    else:
        bfs(x1, y1, l, s)
        print(s[x2][y2])

    
    