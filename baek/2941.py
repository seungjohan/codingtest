import string


crotia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in crotia:
    word = word.replace(i, '*')

print(len(word))