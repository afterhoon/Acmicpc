## 암호
## https://www.acmicpc.net/problem/1855

n = int(input())
str = input()
hei = len(str)//n
arr = [[0 for i in range(n)] for j in range(hei)]
cnt = 0
# 문자열을 조건에 따라 표로 옮긴다
for i in range(hei):
    for j in range(n):
        if i%2 == 0:
            arr[i][j] = str[cnt]
        else:
            arr[i][-j-1] = str[cnt]
        cnt += 1

# 좌측부터 세로로 출력한다
for i in range(n):
    for j in range(hei):
        print(arr[j][i], end="")