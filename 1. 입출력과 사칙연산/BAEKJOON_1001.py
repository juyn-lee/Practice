# 백준 1001
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에서 A와 B가 주어진다. (A > 0, B < 10)
A, B= map(int, input().split())

if A > 0 and B < 10:
    print(A-B)