## 골뱅이 찍기 - ㅂ
## https://www.acmicpc.net/problem/23808

n = int(input())
arr = [["@" for i in range(n*5)] for j in range(n*5)]

# ㅂ의 윗부분 사각형을 공백으로 변경
for i in range(n*2):
    for j in range(n*3):
        arr[i][n+j] = " "

# ㅂ의 아랫부분 사각형을 공백으로 변경
for i in range(n):
    for j in range(n*3):
        arr[n*3+i][n+j] = " "

for i in range(n*5):
    for j in range(n*5):
        print(arr[i][j], end="")
    print()
