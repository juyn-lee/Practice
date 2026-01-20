# 백준 2562

import sys

A= []
for i in range(9):
    A.append(int(sys.stdin.readline()))

print(max(A))
print(A.index(max(A))+1)