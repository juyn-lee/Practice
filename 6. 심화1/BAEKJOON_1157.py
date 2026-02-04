# 백준 1157

import sys

S= sys.stdin.readline().strip().upper()
S_list= list(set(S))
word= []

for i in S_list:
    word.append(S.count(i))

if word.count(max(word))>=2:
    print("?")
else:
    print(S_list[word.index(max(word))])