## 달팽이는 올라가고 싶다
## https://www.acmicpc.net/problem/2869

A, B, V = map(int, input().split())
V = V - A
k = 0
if V%(A-B):
    k = 1
day = V//(A-B) + k + 1

print(day)
