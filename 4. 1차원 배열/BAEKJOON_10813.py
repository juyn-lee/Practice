# 백준 10813

# # join함수 사용
# import sys

# N, M= map(int, sys.stdin.readline().split())
# box = list(range(1, N+1))

# for _ in range(M):
#     i, j = map(int, sys.stdin.readline().split())
#     box[i-1], box[j-1] = box[j-1], box[i-1]
# print(" ".join(map(str, box)))

import sys

N, M= map(int, sys.stdin.readline().split())
box = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]
print(*box)