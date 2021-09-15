## 빠른 A+B
## https://www.acmicpc.net/problem/15552

import sys
T = int(sys.stdin.readline().rstrip())
for t in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
