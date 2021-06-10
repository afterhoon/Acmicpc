## 곱셈
## https://www.acmicpc.net/problem/1629

import sys

## 제한시간이 짧기 때문에 단순 재귀함수로는 불가능하므로 분할정복한다
## 각 변수 입력의 최대값이 int 최대값이므로 오버플로우가 일어나므로 각 계산마다 % c를 해준다
def pow(x, n):
    if n == 1:
        return x % c
    
    p = pow(x, n//2)

    if n%2 == 1:
        return p * p * x % c
    elif n%2 == 0:
        return p * p % c

a, b, c = map(int, sys.stdin.readline().rstrip().split())
print(pow(a,b))