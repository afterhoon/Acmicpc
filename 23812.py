## 골뱅이 찍기 - 돌아간 ㅍ
## https://www.acmicpc.net/problem/23812

n = int(input())
arr = [["@" for i in range(n*5)] for j in range(n*5)] # 모든 칸을 @로 채운다

for i in range(n):
    for j in range(n*3):
        arr[i][j+n] = arr[i+n*2][j+n] = arr[i+n*4][j+n] = " " # 공백으로 변경

for i in range(n*5):
    for j in range(n*5):
        print(arr[i][j], end="")
    print()