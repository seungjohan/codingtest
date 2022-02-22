# 알파벳 -> 아스키코드
# 숫자로 비교해서 경우에 따라 출력하기


words = input()
spellings = [0]
alphabet = list(range(97, 123))

# 알파벳 숫자로 바꿔주기
for word in str(words):
    spelling = int(ord(word)) - int(ord('a')) + 1
    spellings.append(spelling)


for i in alphabet:
    # index에 맞게 출력
    for j in range(len(spellings)):
        if i == spellings[j]:
            print(j)
            continue

    # 이외의 경우 모두 0
    print("-1")


# 2
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 


# 3
words = input()
alphabet = list(range(97, 123))

check = [-1] * 26

for i in range(len(words)):
    if check[ord(words[i]) - 97] != -1:
        continue
    else:
        check[ord(words[i]) - 97] = i

print(check)