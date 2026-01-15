# 백준 25314

N= int(input())

if N%4 == 0:
    N=N//4
    for i in range(N):
        print("long",end= " ")
    print("int")
