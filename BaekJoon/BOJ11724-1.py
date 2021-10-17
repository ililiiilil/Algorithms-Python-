import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[], [1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]
#for i in range(m):
#    graph.append(list(map(int, input().split())))
visited = [False] * (n + 1) 

def dfs(graph, v, visited):
    visited[v] = True
    print(visited)
    print(v)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, graph[1][0], visited)

# 깨달음을 얻은 부분이, graph 리스트의 간선 연결 개수가 전체 노드의
# 값보다 작기 때문에 list index 오류가 발생했던것.. 
# 일단은 matrix화 시켜서 문제를 풀긴할텐데.. 이렇게 혹시 풀순없는지 찾아보자.