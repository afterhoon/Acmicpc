## 분수 합
## https://www.acmicpc.net/problem/1735

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())
c, d = map(int, input().split())
g = gcd(a * d + b * c, b * d) # 약분하기 위한 분자와 분모의 최대공약수
print((a * d + b * c) // g, b * d // g)