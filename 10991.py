## 별 찍기 -16
## https://www.acmicpc.net/problem/10991

n = int(input())

# 전체열-열 만큼의 공백을 두고 열만큼의 "* "를 출력한다
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
