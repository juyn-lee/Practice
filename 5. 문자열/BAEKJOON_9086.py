# 백준 9086

import sys

T= int(sys.stdin.readline())
for i in range(T):
    S= str(sys.stdin.readline().strip())
    print(S[0]+S[-1])