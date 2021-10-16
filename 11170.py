## 0의 개수
## https://www.acmicpc.net/problem/11170

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n,m+1):
        num = str(i)
        