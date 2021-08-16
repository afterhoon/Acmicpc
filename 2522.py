## 별 찍기 -12
## https://www.acmicpc.net/problem/2522

# 별을 출력하는 함수
def printStar(k, n):
    for i in range(n-k):
        print(" ", end="")
    for i in range(k):
        print("*", end="")
    print()

# 위 아래로 별을 출력하고
# 그 사이에 star() 함수를 반복한다
# (한 줄에 n만큼의 별이 출력될때까지 반복)
def star(k, n):
    printStar(k, n)
    if k == n:
        return
    star(k+1, n)
    printStar(k, n)

n = int(input())
star(1, n)