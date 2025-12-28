# 백준 1005

import sys
from collections import deque

input= sys.stdin.readline
T= int(input())

for _ in range(T):
    N, K= map(int, input().split())
    time= list(map(int, input().split()))
    graph= [[] for _ in range(N+1)]
    indegree= [0]*(N+1)
    for _ in range(K):
        X, Y= map(int, input().split())
        graph[X].append(Y)
        indegree[Y]+= 1
    W= int(input())
    dp= [0]*(N+1)
    q= deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i]= time[i-1]
    while q:
        now= q.popleft()

        if now == W:
            print(dp[W])
            break
        for nxt in graph[now]:
            indegree[nxt]-= 1
            dp[nxt]= max(dp[nxt], dp[now]+time[nxt-1])
            if indegree[nxt] == 0:
                q.append(nxt)