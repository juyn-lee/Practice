# 백준 2525

A, B= map(int, input().split())
C= int(input())

if B+C >= 60:
    A= A + (B+C)/60
    B= (B+C)%60
    if A >= 24:
        A= A-24
        print(int(A), int(B))
    else:
        print(int(A), int(B))
else:
    print(A, B+C)