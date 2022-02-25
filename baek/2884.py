h, m = map(int, input().split())

if h == 0:
    h = 23  
else:
    h -= 1

if m < 45:
    m += 15
else :
    m -= 45


print(h, m)