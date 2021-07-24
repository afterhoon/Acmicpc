## 별 찍기 - 17
## https://www.acmicpc.net/problem/10992

n = int(input())
for i in range(n):
    # 맨 윗줄 (가운데에 별 한개)
    if i == 0:
        for j in range(n-1):
            print(" ", end="")
        print("*")
    # 맨 마지막줄 (n*2-1개의 별)
    elif i == n-1:
        for j in range(n*2-1):
            print("*", end="")
        print()
    # 중간 (별 앞부분에 공백을 둔 후 
    # 중간에 규칙에 맞게 공백을 둔 두 별을 출력한다)
    else:
        for j in range(n-1-i):
            print(" ", end="")
        print("*", end="")
        for j in range(i*2-1):
            print(" ", end="")
        print("*")
    