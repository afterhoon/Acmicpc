## 백대열
## https://www.acmicpc.net/problem/14490

n, m = map(int, input().split(":"))

# 최대공약수 계산
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
l = gcd(n, m)

# 최대공약수로 나눈값을 각각 출력
print(n//l, m//l, sep=":")