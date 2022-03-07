import sys




# 동서남북
dx = [1, -1,0,0]
dy = [0,0,1,-1]


def __init__(self):
    m,n,k = map(int, input().split())

    graph = [[False] * n for _ in range(m)]

    for _ in range(k):
        x1,y1,x2,y2 = map(int, input().split())
        for i in range(x1,x2):
            for j in range(y1,y2):
                graph[i][j] = True
