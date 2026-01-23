# 백준 1546

import sys

M = int(sys.stdin.readline())
N= list(map(int, sys.stdin.readline().split()))

print(sum(N)/M*100/max(N))