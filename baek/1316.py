import sys

N = int(input())
result = N
words = []

for i in range(0, N):
    words.append(str(sys.stdin.readline().rstrip()))
    # word = input()

    for j in range(0, len(words[i])-1):
        if words[i][j] != words[i][j+1]:
            pass
        elif words[i][j] == words[i][j+1:]:
            result -= 1
            break

print(words)
print(N)