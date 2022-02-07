import sys

N = int(input())
result = N
words = []

for i in range(0, N):
    words.append(str(sys.stdin.readline().rstrip()))
    # word = input()
    


print(words)
print(N)



# Blog

# N = int(input())
# result = N
# for i in range(0,N):
#     word=input()
#     for j in range(0,len(word)-1):
#         if word[j]==word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             result-=1
#             break
# print(result)