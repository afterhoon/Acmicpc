## Combinations
## https://www.acmicpc.net/problem/13239
## x (123 54 실패)
import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    top = 1
    btm = n-k
    for i in range(k+1, n+1):
        top *= i
        if btm > 1:
            if top % btm == 0:
                top //= btm
                btm -= 1
    print(top//math.factorial(btm))
    # print(top)
    # print(math.factorial(btm))
