## 얼마?
## https://www.acmicpc.net/problem/9325

t = int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    for i in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)
    
    
