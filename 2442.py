## 별 찍기 -5
## https://www.acmicpc.net/problem/2442

n = int(input())

for i in range(n):
    # 각 열은 열번호의 역순만큼의 공백과 
    for j in range(n-i-1):
        print(" ", end="")
    
    # 열번호*2-1만큼의 별을 가지고 있다
    for j in range((i+1)*2-1):
        print("*", end="")
    print()