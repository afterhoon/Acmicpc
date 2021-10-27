## 팩토리얼 0의 개수
## https://www.acmicpc.net/problem/1676

from math import factorial
n = int(input())
ft = factorial(n) # n!의 값을 구함
cnt = 0

while ft > 0:
    if ft % 10 != 0: # n!의 맨 뒷 값이 0이 아니면 종료
        break
    ft //= 10
    cnt += 1

print(cnt)

