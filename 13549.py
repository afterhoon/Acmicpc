## 숨바꼭질 3
## https://www.acmicpc.net/problem/13549
## x
n, k = map(int, input().split())
if n < k:
    l = k // n
    r = l + 1
    print(min(k-l*n, r*n-k))
else:
    print(n-k)
