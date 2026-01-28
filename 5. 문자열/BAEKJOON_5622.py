# 백준 5622

import sys

D= sys.stdin.readline().strip()
S= ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
Sec= 0

for str in D:
    for i in S:
        if str in i:
            Sec += S.index(i) + 3

print(Sec)