## 별찍기 -21
## https://www.acmicpc.net/problem/10996

# 홀수줄에는 *부터 짝수줄에는 공백부터 출력한다
# n: 입력된 값, o: 홀수/짝수
def printStar(n, o):
    for i in range(n):
        if o == 0:
            print("*", end="")
        else:
            if i == n-1:
                break
            print(" ", end="")
        o = 1 - o
    print()

n = int(input())

# n이 1이면 *만 출력하고 종료 아니라면 함수를 실행한다
if n == 1:
    print("*")
else:
    for i in range(n):
        printStar(n, 0)
        printStar(n, 1)