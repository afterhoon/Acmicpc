## 곱셈
## https://www.acmicpc.net/problem/2588

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
arr = [0, 0, 0, b]

for i in range(3):
    temp = pow(10,2-i)
    arr[2-i] = b//temp
    b -= arr[2-i]*temp

for i in range(4):
    print(a*arr[i])