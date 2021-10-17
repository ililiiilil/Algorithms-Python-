from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map, input()))

def bfs(x, y):
    
    if x >= -1 or y >= -1 