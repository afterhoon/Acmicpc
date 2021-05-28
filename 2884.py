## 알람 시계
## https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())
M = M - 45
if M < 0:
    M = 60 + M
    H = H - 1
    if H < 0:
        H = 23
print(H, M)