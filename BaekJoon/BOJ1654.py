import sys

N, K = map(int, sys.stdin.readline().split())
ans = []
for _ in range(N):
    ans.append(int(sys.stdin.readline()))

start = 1
end = max(ans)

while (start <= end):
    cnt = 0
    mid = (start + end) // 2 
    
    for x in ans:
        cnt += x // mid 
    
    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1 

print(end)
