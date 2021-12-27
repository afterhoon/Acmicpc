## 수빈이와 수열
## https://www.acmicpc.net/problem/10539

n = int(input())
b = list(map(int, input().split()))
_sum = 0
for i in range(n):
    temp = b[i] * (i+1)
    _sum += temp - _sum
    print(_sum)
