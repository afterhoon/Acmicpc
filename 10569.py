## 다면체
## https://www.acmicpc.net/problem/10569

t = int(input())
for _ in range(t):
    v, e = map(int ,input().split())
    print(2 - v + e)