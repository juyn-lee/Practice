# 백준 1011

import math

T= int(input())
for _ in range(T):
    X, Y= map(int, input().split())
    d= Y-X
    k= int(math.sqrt(d))
    if d==k**2:
        print(2*k-1)
    elif d<=k*(k+1):
        print(2*k)
    else:
        print(2*k+1)