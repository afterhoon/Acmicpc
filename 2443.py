## 별 찍기 -6
## https://www.acmicpc.net/problem/2443

n = int(input())
# 왼쪽의 공백은 1씩 증가하고
# 별은 n*2-1 에서 2씩 감소한다
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range((n-i)*2-1):
        print("*", end="")
    print()