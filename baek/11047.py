import sys

N, K = map(int, input().split())
coin = []
count = 0

for i in range(0, N):
    coin.append(int(sys.stdin.readline().rstrip()))

# while & Need to check if it is Empty

# while K > 0:
#     target = coin.pop()
#     count += K // target
#     K %= target


# if - for
for i in range(N-1, 0, -1):
    count += K // coin[i]
    K %= coin[i]



print(count)



