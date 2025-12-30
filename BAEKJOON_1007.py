# 백준 1007

import math
from itertools import combinations

T= int(input())
for _ in range(T):
    N= int(input())
    points= [0 for _ in range(N)]
    xtotal, ytotal= 0, 0
    for i in range(N):
        x, y= map(int, input().split())
        xtotal+=x
        ytotal+=y
        points[i]= (x, y)

    min_scala= 1000000
    for c in combinations(range(N), N//2):

        xsum, ysum= 0, 0
        for i in c:
            xsum+=points[i][0]
            ysum+=points[i][1]

        xsum-=xtotal-xsum
        ysum-=ytotal-ysum

        scala= math.sqrt(xsum**2+ysum**2)
        if min_scala>scala:
            min_scala=scala

    print(min_scala)