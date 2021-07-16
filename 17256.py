## 달달함이 넘쳐흘러
## https://www.acmicpc.net/problem/17256

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

# 계산을 역산하면 쉽게 해결된다
print(cx-az, cy//ay, cz-ax)