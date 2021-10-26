## 쿠키애호가
## https://www.acmicpc.net/problem/11134

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    print(n//c + (1 if n%c>0 else 0)) # 올림처리