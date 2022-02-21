n = int(input())
roads = list(map(str, input().split()))
x, y = 1, 1

steps = ['R', 'D', 'L', 'U']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for road in roads:
    for i in range(len(steps)):
        if road == steps[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)