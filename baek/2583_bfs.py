from collections import deque

m, n, k = map(int, input().split())

# up, down, left, right
dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = [list([0] * n) for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())