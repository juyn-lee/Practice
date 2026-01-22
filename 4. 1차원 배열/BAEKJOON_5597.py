# 백준 5597

import sys

N= list(range(1, 31))
for i in range(28):
    N.remove(int(sys.stdin.readline()))
if N[0] > N[1]:
    print(N[1])
    print(N[0])
else:
    print(N[0])
    print(N[1])