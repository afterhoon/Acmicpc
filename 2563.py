## 색종이
## https://www.acmicpc.net/problem/2563

n = int(input())
arr = [[0 for i in range(101)] for j in range(101)]
res = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1

for i in range(101):
    res += arr[i].count(1)
print(res)