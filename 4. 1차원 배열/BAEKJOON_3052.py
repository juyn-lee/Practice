# 백준 3052

import sys

N= list(range(10))
for i in range(10):
    N[i]= int(sys.stdin.readline())%42
print(len(set(N)))