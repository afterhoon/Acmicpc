## 이항 계수
## https://www.acmicpc.net/problem/11050

import math
n, k = map(int, input().split())

# 이항계수의 공식은 n! / (n-k)!k! 이다
print(math.factorial(n)//(math.factorial(n-k)*math.factorial(k)))
