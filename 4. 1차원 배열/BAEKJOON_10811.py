# 백준 10811

import sys

N, M = map(int, sys.stdin.readline().split())

N= list(range(1, N+1))

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    N[a-1:b] = N[a-1:b][::-1]

print(*N)