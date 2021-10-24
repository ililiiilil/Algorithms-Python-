import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(tree)

while start <= end:
    total = 0 
    mid = (start + end) // 2 

    for i in tree:
        if i > mid:
            total += i - mid 
    
    if total >= m:
        start = mid + 1 
    else:
        end = mid - 1 

print(end)