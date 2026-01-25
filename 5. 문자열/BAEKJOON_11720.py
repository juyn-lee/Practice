# 백준 11720

import sys

N= int(sys.stdin.readline())
X= sys.stdin.readline().strip()

sum=0
for i in range(N):
    sum += int(X[i])

print(sum)