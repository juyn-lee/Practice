# 백준 10809

import sys

S= sys.stdin.readline().strip()

for i in range(26):
    print(S.find(chr(ord('a') + i)), end=' ')