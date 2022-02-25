import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True