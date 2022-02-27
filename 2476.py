## 주사위 게임
## https://www.acmicpc.net/problem/2476

n = int(input())
ans = 0
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    temp = 0
    if a == b == c:
        temp = 10000 + a * 1000
    elif a == b:
        temp = 1000 + a * 100
    elif b == c:
        temp = 1000 + b * 100
    elif c == a:
        temp = 1000 + c * 100
    else:
        temp = max(a, b, c) * 100

    ans = max(ans, temp)

print(ans)