import sys

N = int(input())
card = {}

for i in range(0, N):
    num = int(sys.stdin.readline().rstrip())
    if num in card:
        card[num] += 1
    else:
        card[num] = 1

# for i in range(N-1, 1, -1):
#     if card[i-1] >= card[i]:
#         target = card[i-1]

# print(target)

print(sorted(card.items(), key= lambda x: (x[1], -x[0]), reverse=True)[0][0])