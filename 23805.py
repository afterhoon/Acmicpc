## 골뱅이 찍기 - 돌아간 ㄹ
## https://www.acmicpc.net/problem/23805

n = int(input())
arr = [["@" for i in range(n*5)] for j in range(n*5)] # @로 리스트를 채운다

for i in range(n):
    for j in range(n*4):
        arr[j+n][i+n] = arr[j][i+n*3] = " " # ㄹ에서 비는부분을 공백으로 변경해준다

for i in range(n*5):
    for j in range(n*5):
        print(arr[i][j], end="")
    print()