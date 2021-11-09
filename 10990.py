## 별 찍기 - 15
## https://www.acmicpc.net/problem/10990

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    if i == 0: # 첫 라인은 별이 1개이다
        print("*",end="")
    else: # 두번째 라인부터는 별과 별 사이에 공백이 있다
        print("*", end="")
        for j in range(i*2-1):
            print(" ", end="")
        print("*", end="")
    print()

