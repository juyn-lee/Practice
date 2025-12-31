# 백준 1009

# T= int(input())

# for _ in range(T):
#     A, B= map(int, input().split())
#     x= A**B
#     if 1 <= A <= 100 and 1 <= B <= 1000000:
#         print(x%10)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    com = pow(A, B, 10)
    if com == 0:
        print(10)
    else:
        print(com)