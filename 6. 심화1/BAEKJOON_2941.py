# 백준 2941

import sys

S= sys.stdin.readline().strip()

croatia= ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    S= S.replace(i, "*")
    
print(len(S))