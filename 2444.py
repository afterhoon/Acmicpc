## 별찍기-7
## https://www.acmicpc.net/problem/2444

# 재귀적으로 중심으로 갈수록 별개수를 늘려간뒤 최대개수에서 출력후 함수를 종료한다
def func(n, k):
    if n == k:
        printStar(n,k)
        return
    printStar(n,k)
    func(n+1, k)
    printStar(n,k)

# 정해진 수만큼 별을 출력하는 함수
def printStar(n, k):
    for i in range(k-n):
        print(" ", end="")
    for i in range(2*n-1):
        print("*", end="")
    print()

n = int(input())
func(1,n)
