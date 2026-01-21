# 백준 10810

import sys

result =[]

N, M= map(int, sys.stdin.readline().split())
box = [0]*N

for _ in range(M) :
    i,j,k = list(map(int, sys.stdin.readline().split()))
    for i in range(i, j+1):
        box[i-1] = k
for i in range(N):
    result.append(box[i])
print(" ".join(map(str, result)))