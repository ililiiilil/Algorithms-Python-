from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or ny < 0 or nx >= n or ny >= 0:
                    continue
                
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    bfs(0, 0)

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]

#일단 그냥 따라써봤음. 다시한번 풀어보기