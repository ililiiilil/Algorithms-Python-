from collections import deque

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny <= m:
            continue 

        if matrix[nx][ny] == 0:
            continue 

        if matrix[nx][ny] == 1:
            matrix[nx][ny] = matrix[x][y] + 1
            q.append((nx, ny)) 

print(matrix[n - 1][m - 1])
print(matrix)