## 최소공배수
## https://www.acmicpc.net/problem/1934

# 유클리드 호제법으로 최대공약수를 구함
def gcd(x, y):
    # y가 0이 될때까지 반복한다
    while y:
        # x에 y를 y에 x/y의 나머지를 대입
        x, y = y, x % y
    # x(최대공약수)를 출력한다
    return x

def lcm(x, y):
    # x*y에는 최대공약수가 2번 곱해져 있으므로 최대공약수를 한번 나누어 준다
    # (정수로 출력하기 위해 /가 아닌 //로 계산)
    return x * y // gcd(x, y)

T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    print(lcm(x, y))