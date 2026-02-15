# 백준 1316

import sys

N= int(sys.stdin.readline().strip())
count = N

for i in range(N):
    word= sys.stdin.readline().strip()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break
print(count)
