# 백준 3003

import sys

white= list(map(int, sys.stdin.readline().split()))
chess= [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(chess[i]-white[i], end=" ")