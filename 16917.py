## 양념 반 후라이드 반
## https://www.acmicpc.net/problem/16917

a, b, c, x, y = map(int, input().split())

if a + b < c * 2:
    print(a * x + b * y)
else:
    print(c * min(x, y) * 2 + min(c * 2, a) * max(0, x - min(x, y)) + min(c * 2, b) * max(0, y - min(x, y)))