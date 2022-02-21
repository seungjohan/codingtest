cor = input()
row = int(cor[1])
col = int(ord(cor[0])) - int(ord('a')) + 1

# Can not get out of the chess board 
# 경우의 수 체크

count = 0
steps = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]

    if nrow * ncol <= 0 or nrow > 8 or ncol > 8:
        continue
    count += 1



print(count)
