num, pivot = map(int, input().split())

number = list(map(int, input().split()))


for i in range(num):
    if number[i] < pivot:
        print(number[i], end= ' ')