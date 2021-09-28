## 구간 합 구하기 5
## https://www.acmicpc.net/problem/11660
# 시간초과
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for j in range(y1-1, y2):
        for k in range(x1-1, x2):
            sum += arr[j][k]

    print(sum)