# 백준 2675

import sys

T= int(sys.stdin.readline())

for i in range(T):
    R, S= sys.stdin.readline().split()
    R= int(R)
    for j in range(len(S)):
        print(S[j] * R, end='')
    print()