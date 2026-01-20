# 백준 10807

import sys

N= int(sys.stdin.readline())
A= list(map(int, sys.stdin.readline().split()))
V= int(sys.stdin.readline())

print(A.count(V))