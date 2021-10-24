N, M = map(int, input().split())

visited = [0] * N
ans = [] 

def sol(depth, N, M):
    if depth == M:
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1 
            ans.append(i + 1)
            sol(depth + 1, N, M)
            visited[i] = 0 
            ans.pop()
    
sol(0, N, M)