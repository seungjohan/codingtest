n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort()

biggest = data[n-1]
biggest2 = data[n-2]

result = 0

while True:
    
    for i in range(k):
        if m == 0:
            break
        result += biggest
        m -= 1
    if m == 0:
        break
    result += biggest2
    m-=1

print(result)
