from re import L


number = int(input())
stack = []
result = 0

for i in range(number):

    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

# for i in range(len(stack)):
#     result += stack[i]
# print(result)
print(sum(stack))