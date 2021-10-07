## 별 찍기 - 10
## https://www.acmicpc.net/problem/2447
# X (시간초과)

def printStar(i, j, n):
    if (i//n) % 3 == 1 and (j//n) % 3 == 1:
        print(end=" ")
    else:
        if n // 3 == 0:
            print("*", end="")
        else:
            printStar(i,j,n//3)

n = int(input())
# "*" 혹은 " " 이 들어갈수있는 각 position에서 
# 무엇을 출력할지 정하는 printStar() 함수를 호출한다
for i in range(n):
    for j in range(n):
        printStar(i,j,n)
    print()