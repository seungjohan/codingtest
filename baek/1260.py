import sys
from collections import deque

def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in graph[n]:
            if not visited:
                queue.append(n)
                visited[i] = True


def dfs(n):
    visited[n] = True
    print(n, end=' ')


    for i in graph[n]:
        if not visited:
            dfs(graph, i, visited)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


# make adjacency list
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# sort adjacency list
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
# initialize check list
visited = [False] * (n + 1)
bfs(v)