## 전북대학교
## https://www.acmicpc.net/problem/14624

def printStar(k, l): #삼각형 모양으로 별 출력
    print(" "*(k-l-1), "*", " "*(l*2-1), "*" if l != 0 else "", sep="")

n = int(input())
if n % 2 == 0: #짝수면 문장을 출력하고 종료한다
    print("I LOVE CBNU")
else: #맨 윗줄에는 n만큼 별을 출력하고 그 이후부터 형식에 맞게 출력
    print("*"*n)
    for i in range(n//2+1):
        printStar(n//2+1, i)


            