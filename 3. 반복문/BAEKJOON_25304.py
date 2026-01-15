# 백준 25304

X= int(input())
N= int(input())

for i in range(1, N+1):
    A, B= map(int, input().split())
    X= X - A*B
if X==0:
    print("Yes")
else:
    print("No")