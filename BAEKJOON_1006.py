# 백준 1006

# def solve(i):
#   DP = [[2*N]*(N+1) for i in range(4)]; DP[i][-1] = 0
#   for n in range(N):
#     for i in range(4):
#       DP[0][n]= min(DP[0][n],DP[i][n-1]+int(i&1==0)+int(i&2==0))
#     if enemy[0][n]+enemy[1][n]<=M:
#       DP[0][n]= min(DP[0][n],DP[0][n-1]+1)
#     if enemy[0][n]+enemy[0][n+1]<=M:
#       DP[1][n]= min(DP[0][n-1]+2,DP[2][n-1]+1)
#     if enemy[1][n]+enemy[1][n+1]<=M:
#       DP[2][n]= min(DP[0][n-1]+2,DP[1][n-1]+1)
#     if enemy[0][n]+enemy[0][n+1]<=M and enemy[1][n]+enemy[1][n+1]<=M:
#       DP[3][n]= DP[0][n-1]+2
#   return DP

# for _ in range(int(input())):
#   N,M = map(int,input().split())
#   enemy = [[*map(int,input().split()),0] for i in range(2)]
#   result = solve(0)[0][N-1]
#   if enemy[0][0]+enemy[0][N-1]<=M:
#     DP = solve(1)
#     result = min(result,DP[2][N-2]+1,DP[0][N-2]+2)
#   if enemy[1][0]+enemy[1][N-1]<=M:
#     DP = solve(2)
#     result = min(result,DP[1][N-2]+1,DP[0][N-2]+2)
#   if enemy[0][0]+enemy[0][N-1]<=M and enemy[1][0]+enemy[1][N-1]<=M:
#     result = min(result,solve(3)[0][N-2]+2)
#   print(result)

import sys

T= int(sys.stdin.readline())
results= []

def recur(start, a, b, c):
    for i in range(start, N):
        a[i+1]= min(b[i]+1, c[i]+1)
        if zone1[i]+zone2[i] <= W: a[i+1]= min(a[i+1], a[i]+1)
        if i > 0 and zone1[i-1]+zone1[i] <= W and zone2[i-1]+zone2[i] <= W: a[i+1]= min(a[i+1], a[i-1]+2)

        if i < N-1:
            b[i+1]= a[i+1]+1
            if zone1[i+1]+zone1[i] <= W: b[i+1]= min(b[i+1], c[i]+1)

            c[i+1]= a[i+1]+1
            if zone2[i+1]+zone2[i] <= W: c[i+1]= min(c[i+1], b[i]+1)
    
    return a, b, c


for _ in range(T):
    N, W= map(int, sys.stdin.readline().split())
    zone1= list(map(int, sys.stdin.readline().split()))
    zone2= list(map(int, sys.stdin.readline().split()))
    
    a= [0 for _ in range(N+1)]
    b= [0 for _ in range(N+1)]
    c= [0 for _ in range(N+1)]
    a[0]= 0
    b[0]= 1
    c[0]= 1
    a, b, c= recur(0, a, b, c)
    res= a[N]
	
    if N > 1 and zone1[0]+zone1[N-1] <= W:
        a[1]= 1
        b[1]= 2
        if zone2[0]+zone2[1] <= W: c[1]= 1
        else: c[1]= 2
        
        a, b, c= recur(1, a, b, c)
        res= min(res, c[N-1]+1)
        
    if N > 1 and zone2[0]+zone2[N-1] <= W:
        a[1]= 1
        c[1]= 2
        if zone1[0]+zone1[1] <= W: b[1]= 1
        else: b[1]= 2
        
        a, b, c= recur(1, a, b, c)
        res= min(res, b[N-1] + 1)

    if N > 1 and zone1[0]+zone1[N-1] <= W and zone2[0]+zone2[N-1] <= W:
        a[1]= 0
        b[1]= 1
        c[1]= 1

        a, b, c= recur(1, a, b, c)
        res= min(res, a[N-1]+2)
    
    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')