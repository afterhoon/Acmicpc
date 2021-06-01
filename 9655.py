## 돌 게임
## https://www.acmicpc.net/problem/9655

import sys

N = int(sys.stdin.readline())

## 각 돌 개수에 따른 승자를 정리하면
## 1 2 3 4 5 6 ...
## S C S C S C ...
## 1개 혹은 3개만 가져갈수 있으므로 반드시 홀수번에는 상근, 짝수번에는 창영이 이긴다
if N % 2 == 1:
    print("SK")
else:
    print("CY")