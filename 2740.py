## 행렬 곱셈
## https://www.acmicpc.net/problem/2740

a = []
b = []

n, m = map(int, input().split())
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
for _ in range(m):
    b.append(list(map(int, input().split())))

res = [[0 for i in range(k)] for j in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j] += a[i][l] * b[l][j]

for i in range(n):
    print(" ".join(map(str, res[i])))