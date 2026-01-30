# 백준 10988

import sys

S = sys.stdin.readline().strip()
if S == S[::-1]:
    print(1)
else:
    print(0)