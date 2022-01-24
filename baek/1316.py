import string
import sys

N = int(input())
words = []

for i in range(0, N):
    words.append(string(sys.stdin.readline().rstrip()))

    