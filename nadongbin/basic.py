import time
start = time.time()

array = [3,5,1,2,4]

for i in array:
    for j in array:
        temp = i* j
        print(temp)


end = time.time()

print("time : ", end - start)