num = int(input())

ci, cj ,ck = 0, 0, 0
count = 0
# 00시 00분 00초
# num 숫자포함

for i in range(num + 1):
    for j in range(60):
        for k in range(60):
            if str(num) in str(i) + str(j) + str(k):
                count += 1
print(count)
