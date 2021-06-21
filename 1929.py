## 소수 구하기
## https://www.acmicpc.net/problem/1929

import math
m, n = map(int, input().split())

def isPrime(m, n):
    prime = [True] * n
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in range(2*i, n, i):
                prime[j] = False

    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)

isPrime(m, n+1)